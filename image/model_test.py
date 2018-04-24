import unittest
from image.model import Image2D


class TestImage(unittest.TestCase):

    def setUp(self):
        self.img = Image2D()

    def test_is4Connected(self):
        self.assertFalse(self.img.is4Connected((1, 1), (2, 2)))

    def test_is8Connected(self):
        self.assertTrue(self.img.is8Connected((1, 1), (2, 2)))

    def test_isMConnected(self):
        self.assertFalse(self.img.isMConnected((1, 1), (2, 2)))
