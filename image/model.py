from skimage import io,data
from math import fabs


class Image2D(object):

    def __init__(self, path=None):
        self.path = path
        if path != None:
            self.data = io.imread(path)
        else:
            self.data = data.checkerboard()

    def is4Connected(self, p1, p2):
        """

        :param p1: position if p1, eg. (x, y)
        :param p2:
        :return: if pixel p1 and p2 is four-connected
        """
        if self.pixel(p1[0], p1[1]) ==  self.pixel(p2[0], p2[1]):
            return 1 == fabs(p1[0] - p2[0]) + fabs(p1[1] - p2[1])
        return False

    def pixel(self, x, y):
        if x >= 0 and y >= 0 and x < self.data.shape[0] and y < self.data.shape[1]:
            return self.data[x][y]

    def is8Connected(self, p1, p2):
        """

        :param p1:
        :param p2:
        :return:
        """
        if self.pixel(p1[0], p1[1]) == self.pixel(p2[0], p2[1]):
            return 1 <= fabs(p1[0] - p2[0]) + fabs(p1[1] - p2[1]) <= 2
        return False

    def isMConnected(self, p1, p2):
        """

        :param p1:
        :param p2:
        :return:
        """
        if self.is4Connected(p1, p2):
            return True
        elif self.is8Connected(p1, p2):
            if self.is4Connected(p1, (p1[0], p2[1])) or self.is4Connected(p1, (p2[0], p1[1])):
                return False
            else:
                return True
        return False
