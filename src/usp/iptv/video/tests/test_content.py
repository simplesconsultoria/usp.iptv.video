# -*- coding: utf-8 -*-

from plone import api
from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID
from usp.iptv.video.interfaces import IVideo
from usp.iptv.video.testing import INTEGRATION_TESTING
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ContentTypeTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        with api.env.adopt_roles(['Manager']):
            self.folder = api.content.create(self.portal, 'Folder', 'folder')

        self.video = api.content.create(self.folder, 'Video', 'video')

    def test_adding(self):
        self.assertTrue(IVideo.providedBy(self.video))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Video')
        self.assertIsNotNone(fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Video')
        schema = fti.lookupSchema()
        self.assertEqual(IVideo, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Video')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IVideo.providedBy(new_object))

    def test_is_referenceable(self):
        self.assertTrue(IReferenceable.providedBy(self.video))
        self.assertTrue(IAttributeUUID.providedBy(self.video))
