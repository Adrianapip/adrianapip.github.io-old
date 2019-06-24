#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adriana'
SITEURL = ''
SITENAME = "Adriana Patterson Ip"
SITETITLE = "Adriana Patterson Ip"
SITESUBTITLE = "Science || Coding || Baking"
COPYRIGHT_NAME = 'Adriana Patterson Ip,'
COPYRIGHT_YEAR = '2019'
SITELOGO = SITEURL + '/img/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

PATH = '/Users/adrianaip/Amazon_Drive/Side_Projects/adrianapip.github.io/content/'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('??', 'https://github.com/Adrianapip'))
        

# Social widget
SOCIAL = (('github', 'https://github.com/Adrianapip'),
          ('twitter', 'https://twitter.com/aspatterson'),
          ('linkedin', 'https://www.linkedin.com/in/adrianaip/'))

DEFAULT_PAGINATION = 10

THEME = '/Users/adrianaip/Amazon_Drive/Side_Projects/adrianapip.github.io/pelican-themes/Flex'
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['img', 'static', 'pdfs', 'extra/CNAME',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['readtime']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True