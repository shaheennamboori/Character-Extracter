from PIL import Image

def _openImage(im):
    return Image.open(im)

def processImage(im):
    img = _openImage(im)
    # garyscale
    img = img.convert('L')
    # threshold
    threshold = 140
    img = img.point(lambda p: p > threshold and 255)  

    # show
    img.show()