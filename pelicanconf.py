#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adriana'
SITEURL = 'http://www.adrianapattersonip.com'
SITENAME = "Adriana Patterson Ip"
SITEURL = ''
SITETITLE = 'Adriana Patterson Ip'
SITESUBTITLE = "I'm a scientist that likes to code and bake pies."
COPYRIGHT_NAME = 'Adriana Patterson Ip,'
COPYRIGHT_YEAR = '2019'
SITELOGO = SITEURL + '/img/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'

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
LINKS = ()
        

# Social widget
SOCIAL = (('github', 'https://github.com/Adrianapip'),
          ('twitter', 'https://twitter.com/aspatterson'),
          ('linkedin', 'https://www.linkedin.com/in/adrianaip/'))

DEFAULT_PAGINATION = 10

THEME = '/Users/adrianaip/pelican-themes/Flex'
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['img', 'static', 'pdfs']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True