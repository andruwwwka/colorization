# coding: utf-8
import hashlib
import mimetypes
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.timezone import now
from django.views.generic import TemplateView

from convert.models import Convert
from convert.tasks import run


class HomeView(TemplateView):
    """
    Класс представления домашней страницы
    """
    template_name = "index.html"
    post_template = "message.html"
    alt_post_template = "message-alt.html"
    email_template = "input_email.html"

    def post(self, request):
        ctx = dict()
        render_to = self.template_name
        if request.POST.get('email'):
            convert_id = int(request.POST.get('convert_id'))
            convert = Convert.objects.get(id=convert_id)
            # Ставим в очередь конвертацию изображения. Только по результату конвертации отправляем письмо
            run.delay(convert=convert, email=request.POST.get('email'), template=self.post_template, alt_template=self.alt_post_template)
        elif request.FILES.dict().get('source') and request.FILES.dict().get('marked'):
            new_convert = Convert(
                source_file=request.FILES['source'],
                marked_file=request.FILES['marked'],
                convert_time=now()
            )
            hashed = hashlib.new('ripemd160')
            hashed.update(new_convert.source_file.name)
            new_convert.hashed_name = hashed.hexdigest()
            new_convert.save()
            new_convert.url = 'http://deepcol.com/' + hashed.hexdigest()
            new_convert.save()
            render_to = self.email_template
            ctx['convert_id'] = new_convert.id
        return render_to_response(render_to, ctx, context_instance=RequestContext(request))

    def get(self, request, *args, **kwargs):
        return render_to_response('index.html', dict(), context_instance=RequestContext(request))


class ResultImage(TemplateView):
    """
    Класс представления страницы результата
    """
    template_name = 'result.html'

    def get_context_data(self, hash_str, **kwargs):
        ctx = super(ResultImage, self).get_context_data(**kwargs)
        result_convert = Convert.objects.get(hashed_name=hash_str)
        ctx['hash_str'] = result_convert.hashed_name
        ctx['url_color'] = result_convert.destination_file.name.replace('static/', '')
        ctx['url_black'] = result_convert.source_file.name.replace('static/', '')
        return ctx

    def post(self, request, convert_id, *args, **kwargs):
        result_convert = Convert.objects.get(id=convert_id)
        like = request.POST.get('like')
        if like:
            result_convert.mark = True if like == "true" else False
            result_convert.save()
            return True
        out = BytesIO(result_convert.destination_file.file.read())
        content_type = mimetypes.guess_type(result_convert.destination_file.path)[0]
        return HttpResponse(out.getvalue(), content_type=content_type)
