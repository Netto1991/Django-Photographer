from django.test import TestCase
from fotopage.models import Album

class AlbumModelTest(Testcase):
    def SetUpTestData(cls):
        Album.object.create(title = 'My album', thumb = )
    @classmethod
    def