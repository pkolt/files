====================================================================
Files. The total loading mechanism (attachment) files for the models
====================================================================

Depending
- uploadtools (http://github.com/pkolt/)


Installing
1. Add 'files' in INSTALLED_APPS
3. python manage.py syncdb


Integration (for example Flatpages)
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
