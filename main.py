# from image.model import Image2D
# from image import model
# from image.model import *
import image.model as m


if __name__ == "__main__":
    img = m.Image2D()
    print(img.data.shape)