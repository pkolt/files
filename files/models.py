#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from pkoltutils.models import generic_upload_to

class File(models.Model):
    " Файлы "
    created = models.DateTimeField(verbose_name=u"Создано", auto_now_add=True)
    file = models.FileField(verbose_name=u"Файл", upload_to=lambda i,f: generic_upload_to(i,f,'content_type'))
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.file.url if self.file else ''
    
    class Meta:
        ordering = ('-created',)
        verbose_name = u"Файл"
        verbose_name_plural = u"Файлы"