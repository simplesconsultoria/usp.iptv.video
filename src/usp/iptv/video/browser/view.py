# -*- coding: utf-8 -*-

from five import grok
from usp.iptv.video.interfaces import IVideo

grok.templatedir('templates')


class HelloWorld (grok.view):
    """Browserview de exemplo Hello World
    """

    grok.context(IVideo)
