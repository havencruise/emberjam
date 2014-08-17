from optparse import make_option
from django.conf import settings
from django.core.management.base import AppCommand, CommandError
import os
import shutil

MEDIA_DIRS = ['js', 'css', 'img', 'swf']

WINDOWS = False
if os.name in ('nt', 'dos'):
    WINDOWS = True

class Command(AppCommand):

    option_list = AppCommand.option_list + (
        make_option('--force', action='store_true', dest='force', default=False,
            help='Remove existing files and copy app media files again.'),
        )


    help = "Copies any app's specific media files over to media_root directory"
    args = '[appname ...]'

    def handle_app(self, app, **options):

        verbosity = int(options.get('verbosity'))

        app_media_dir =  "%s/static/%s" % (
                            "/".join(app.__file__.split('/')[:-1]),
                            app.__package__)
        if WINDOWS:
            app_media_dir =  "%s\\static" % "\\".join(app.__file__.split('\\')[:-1])


        app_name = app.__name__.split('.')[-2]
        media_dir = '%s/%s' % (settings.STATIC_ROOT, app_name)

        if not os.path.exists(app_media_dir):
            if verbosity > 0:
                print 'App %s does not have a media directory' % (app_name)
            return

        force = options.get('force')

        if os.path.exists(media_dir) and force:
            shutil.rmtree(media_dir)

        if os.path.exists(media_dir):
            if verbosity > 0:
                print 'Media directory %s already exists in %s' % (app_name, settings.MEDIA_ROOT)
        else:
            os.mkdir(media_dir)
            for i in MEDIA_DIRS:
                if WINDOWS:
                    if os.path.exists("%s\\%s"  % (app_media_dir, i)):
                        print "Copying %s\\%s to %s" % (app_media_dir, i, media_dir)
                        shutil.copytree("%s\\%s" % (app_media_dir, i), "%s\\%s" % (media_dir, i), ignore=shutil.ignore_patterns('.svn'))
                else:
                    if os.path.exists("%s/%s" % (app_media_dir, i)):
                        print "Copying %s/%s to %s" % (app_media_dir, i, media_dir)
                        shutil.copytree("%s/%s" % (app_media_dir, i), "%s/%s" % (media_dir, i), ignore=shutil.ignore_patterns('.svn'))
