#!/usr/bin/env python
import sys
import os
import shutil
import glob


NAME = sys.argv[0]

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
TEMPLATES_DIR = "%s/conf/.framework/templates" % BASE_DIR
RESOURCES_DIR = "%s/resources" % BASE_DIR
MEDIA_DIR = "%s/%s" % (BASE_DIR, "media")
STATIC_DIRS = ("js", "swf", "css", "img")

SITE_DIR = '%s/%s', (BASE_DIR, 'default_name')


def dir_exists(name, directory):
    path = "%s/%s" % (directory, name)
    return os.path.exists(path)


def create_site(name,
                directory=SITE_DIR,
                templates_dir=TEMPLATES_DIR,
                static_dir=RESOURCES_DIR,
                media_dir=MEDIA_DIR):

    if not directory:
        sys.stderr.write(
            "Please provide a site name, e.g. %s <site_name>\n\n" % NAME)
        sys.exit(1)

    site_app_path = '%s/%s' % (directory, name)

    try:
        os.makedirs("%s" % directory)
        sys.stdout.write("\tCreated %s\n" % (directory))

        os.makedirs("%s" % media_dir)
        sys.stdout.write("\tCreated %s\n" % media_dir)
    except:
        pass

    sys.stdout.write("\tCopying site templates to %s\n" % directory)

    files = glob.iglob(os.path.join(templates_dir, "*.py"))
    for _file in files:
        if os.path.isfile(_file):
            shutil.copy2(_file, directory)

    shutil.copytree("%s/site_instance/" % templates_dir,
                    site_app_path,
                    ignore=shutil.ignore_patterns('.svn'))

    site_resources = "%s/%s" % (static_dir, name)

    for static_dir in STATIC_DIRS:
        try:
            os.makedirs("%s/%s" % (site_resources, static_dir))
            sys.stdout.write("\tCreated %s in %s\n" %
                             (static_dir, site_resources))
        except:
            pass


def generate_secret_key(site_name, directory=SITE_DIR):
    from django.utils.crypto import get_random_string
    f = open("%s/%s/settings/app.py" % (SITE_DIR, site_name), "a")
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    f.write("\nSECRET_KEY = '%s'\n" % get_random_string(50, chars))
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(
            "Please provide a site name, e.g. %s <site_name>\n\n" % NAME)
        sys.exit(1)

    site_name = sys.argv[1]

    SITE_DIR = '%s/%s' % (BASE_DIR, site_name)

    if dir_exists(site_name, BASE_DIR):
        sys.stderr.write(
            "Site '%s' already exists in %s\n\n" % (site_name, BASE_DIR))
        sys.exit(1)

    if not dir_exists('', TEMPLATES_DIR):
        sys.stderr.write(
            "Unable to find framework site templates, \
            please update framework for latest files")
        sys.exit(1)

    sys.stdout.write(
        "Creating site '%s' in %s\n" % (site_name, BASE_DIR))

    create_site(site_name, directory=SITE_DIR)

    sys.stdout.write("Creating secret key for '%s' \n" % site_name)
    generate_secret_key(site_name, SITE_DIR)
