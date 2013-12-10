# -*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.directives import form
from usp.iptv.video import _
from zope.interface import Interface


class IBrowserLayer(Interface):
    """Layer especifico para este add-on.

    Esta interface e referenciada em browserlayers.xml.

    Views e viewlets registrados para este layer serao exibidos
    apenas quando o produto estiver instalado.
    """


class IVideo(form.Schema):
    """Exemplo de schema para um tipo de conteúdo."""

    text = RichText(
        title=_(u'Body text'),
        required=False,
    )
