# -*- coding: utf-8 -*-

from five import grok
from plone.dexterity.content import Container
from usp.iptv.video.interfaces import IVideo


class Video(Container):
    """Exemplo de tipo de conteúdo."""

    grok.implements(IVideo)
