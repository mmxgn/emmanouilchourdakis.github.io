#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Emmanouil Theofanis Chourdakis'
SITENAME = 'Emmanouil Theofanis Chourdakis'
SITEURL = 'http://mmxgn.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Nomono', 'https://www.nomono.co'),('Intelligent Sound Engineering', 'https://intelligentsoundengineering.wordpress.com/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/echourdakis/'),
        ('Github', 'https://www.github.com/mmxgn'),
          ('Youtube', 'https://www.youtube.com/user/mmxgn'))

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['img', 'pdf']

LANDING_PAGE_ABOUT="pages/about-me.html"

THEME="/home/mmxgn/git/mmxgn.github.io/theme"
