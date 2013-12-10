# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

PROJECTNAME = 'usp.iptv.video'


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'usp.iptv.video:uninstall',
            u'usp.iptv.video.upgrades.v2000:default'
        ]
