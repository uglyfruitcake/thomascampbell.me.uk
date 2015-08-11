#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas'
SITENAME = u'Thomas Campbell'
SITEURL = 'http://localhost:8000'

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en_GB'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

SOCIAL = (
    ('Google+', 'https://plus.google.com/u/0/115145418718867457256/posts',
        'fa fa-google-plus-square fa-fw fa-lg'),
    # ('Twitter', 'https://twitter.com/opcampbell',
    #     'fa fa-twitter-square fa-fw fa-lg'),
    # ('LinkedIn', 'https://www.linkedin.com/in/owencampbell',
    #     'fa fa-linkedin-square fa-fw fa-lg'),
    # ('BitBucket', 'http://bitbucket.org/meatballs',
    #     'fa fa-bitbucket-square fa-fw fa-lg'),
    ('GitHub', 'http://github.com/uglyfruitcake',
        'fa fa-github-square fa-fw fa-lg'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ('plugins',)
PLUGINS = ['creole_reader', 'render_math' ]

THEME = 'themes/pelican-bootstrap3/'
