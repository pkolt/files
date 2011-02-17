#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.contenttypes import generic
from files.models import File

class FileInline(generic.GenericTabularInline):
    model = File