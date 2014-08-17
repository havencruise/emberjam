from django.conf import settings
from django.core.management import call_command
from django import template
from django.db.models.signals import post_syncdb

if 'pipeline' in settings.INSTALLED_APPS:
    template.add_to_builtins('pipeline.templatetags.compressed')


def sync_app_static(app, **kwargs):
    app_name = app if isinstance(app, basestring) else app.__name__.split('.')[-2]
    call_command('sync_app_static', app_name, verbosity=0)

post_syncdb.connect(sync_app_static)

if 'south' in settings.INSTALLED_APPS:
    from south.signals import post_migrate
    post_migrate.connect(sync_app_static)
