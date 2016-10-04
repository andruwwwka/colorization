# coding: utf-8
import numpy as np
import os
import scipy
from celery import task
from django.core.files import File
from django.core.mail import EmailMultiAlternatives
from django.http import request
from django.template.loader import render_to_string
from scipy import io, misc, sparse
from scipy.sparse.linalg import spsolve
from sklearn.preprocessing import normalize

import cartesian
import color_conv
from main import settings


def neighborhood(x, r):
    d = 1
    l1, h1 = max(r[0]-d, 0), min(r[0] + d + 1, x.shape[0])
    l2, h2 = max(r[1]-d, 0), min(r[1] + d + 1, x.shape[1])
    return x[l1:h1, l2:h2]


def weight(r, v, y, S):
    return [np.exp(-1 * np.square(y[r] - y[v]) / S[r]) if S[r] > 0.0 else 0.0 for v in v]


def find_marked_locations(bw, marked):
    diff = marked - bw
    colored = [set(zip(*np.nonzero(diff[:, :, i]))) for i in [1, 2]]
    return colored[0].union(colored[1])


def std_matrix(a):
    s = np.empty_like(a)
    for i in xrange(a.shape[0]):
        for j in xrange(a.shape[1]):
            s[i, j] = np.square(np.std(neighborhood(a, [i, j])))
    return s


def build_weights_matrix(y):
    (n, m) = [y.shape[0], y.shape[1]]
    s = std_matrix(y)
    size = n * m
    cart = cartesian.cartesian([xrange(n), xrange(m)])
    cart_r = cart.reshape(n, m, 2)
    xy2idx = np.arange(size).reshape(n, m)  # [x,y] -> index
    w = sparse.lil_matrix((size, size))
    for i in xrange(y.shape[0]):
        for j in xrange(y.shape[1]):
            idx = xy2idx[i, j]
            n = neighborhood(cart_r, [i, j]).reshape(-1, 2)
            n = [tuple(neighbor) for neighbor in n]
            n.remove((i, j))
            p_idx = [xy2idx[xy] for xy in n]
            weights = weight((i, j), n, y, s)
            w[idx, p_idx] = -1 * np.asmatrix(weights)

    Wn = normalize(w, norm='l1', axis=1)
    Wn[np.arange(size), np.arange(size)] = 1

    return Wn


@task
def run(convert, email, template, alt_template):
    bw_filename = convert.source_file.name
    marked_filename = convert.marked_file.name
    out_filename = bw_filename.replace('source', 'result')
    matrix_name = 'matrix/' + bw_filename.replace('.bmp', '')[bw_filename.rfind('/'):]

    bw_rgb = misc.imread(bw_filename)
    marked_rgb = misc.imread(marked_filename)

    bw = color_conv.rgb2yiq(bw_rgb)
    marked = color_conv.rgb2yiq(marked_rgb)

    y = np.array(bw[:, :, 0], dtype='float64')

    (n, m) = np.shape(bw)[0:2]  # extract image dimensions
    size = n * m
    wn = 0
    if os.path.isfile(matrix_name + '.mtx'):
        wn = scipy.io.mmread(matrix_name).tocsr()
    else:
        wn = build_weights_matrix(y)
        scipy.io.mmwrite(matrix_name, wn)

    ## once markes are found
    colored = find_marked_locations(bw_rgb, marked_rgb)

    ## set rows in colored indices
    wn = wn.tolil()
    xy2idx = np.arange(size).reshape(n, m)  # [x,y] -> index
    for idx in [xy2idx[i, j] for [i, j] in colored]:
        wn[idx] = sparse.csr_matrix(([1.0], ([0], [idx])), shape=(1, size))

    lu = scipy.sparse.linalg.splu(wn.tocsc())

    b1 = (marked[:, :, 1]).flatten()
    b2 = (marked[:, :, 2]).flatten()

    x1 = lu.solve(b1)
    x2 = lu.solve(b2)

    sol = np.zeros(np.shape(bw_rgb))
    sol[:, :, 0] = y
    sol[:, :, 1] = x1.reshape((n, m))
    sol[:, :, 2] = x2.reshape((n, m))
    sol_rgb = color_conv.yiq2rgb(sol)
    path_name = out_filename[:out_filename.rfind('/')]
    if not os.path.exists(path_name):
        os.makedirs(path_name)
    misc.imsave(out_filename, sol_rgb)

    data = dict()
    html = render_to_string(template, data)
    text = render_to_string(alt_template, data)
    msg = EmailMultiAlternatives(
        subject=u'Преобразование изображения',
        body=text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
        alternatives=[(html, 'text/html')]
    )
    msg.send()
    f = open(out_filename)
    convert.destination_file = out_filename#File(f)
    convert.sended = True
    convert.save()
    f.close()
