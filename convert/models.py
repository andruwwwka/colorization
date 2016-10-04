# coding: utf-8
from django.db import models


class Convert(models.Model):
    """
    Событие конвертации изображения
    """
    hashed_name = models.CharField(
        verbose_name=u'Хэш имени файла',
        max_length=511,
        null=True
    )
    source_file = models.FileField(
        verbose_name=u'Путь к исходному файлу',
        upload_to='static/upload_images/source/%Y/%m/%d'
    )
    """Исходный файл"""
    destination_file = models.FileField(
        verbose_name=u'Путь к результирующему файлу',
        upload_to='static/upload_images/result/%Y/%m/%d'
    )
    marked_file = models.FileField(
        verbose_name=u'Путь к маркированному файлу',
        upload_to='static/upload_images/marked/%Y/%m/%d',
        null=True
    )
    """Результирующий файл"""
    url = models.URLField(
            verbose_name=u'Ссылка на результат',
            max_length=511
    )
    """Ссылка на результирующий файл"""
    convert_time = models.DateTimeField(
        verbose_name=u'Дата конвертации',
    )
    """
    Дата конвертации изображения
    """
    mark = models.NullBooleanField(
        verbose_name=u'Оценка',
        blank=True,
        null=True,
        default=None
    )
    """
    Оценка конвертации
    """
    sended = models.BooleanField(
        verbose_name=u'Письмо отправлено',
        blank=True,
        default=False
    )
