from PIL import Image

def _openImage(im):
    return Image.open(im)

def processImage(im):
    img = _openImage(im)
    img.show()