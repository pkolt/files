# Django приложение Files

Общий механизм загрузки(вложения) файлов для моделей

## Зависимости

1. pkoltutils (https://github.com/pkolt/pkoltutils)
2. trans (http://pypi.python.org/pypi/trans/1.2)


## Установка приложения

1. Скопировать приложение в папку проекта
2. Добавить 'files' в INSTALLED_APPS
3. Выполнить python manage.py syncdb


## Интеграция (на примере Flatpages)

    # admin.py
    from django.contrib import admin
    from django.contrib.contenttypes import generic
    from django.contrib.flatpages.models import FlatPage
    from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
    from files.admin import FileInline

    class FlatPageAdmin(FlatPageAdminOld):
        inlines = [FileInline,]

    admin.site.unregister(FlatPage)
    admin.site.register(FlatPage, FlatPageAdmin)
