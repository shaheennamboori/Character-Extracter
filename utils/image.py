from PIL import Image,ImageFilter
# import numpy as np

def _openImage(im):
    return Image.open(im)

def processImage(im):
    img = _openImage(im)
    # garyscale
    img = img.convert('L')
    # threshold
    threshold = 160
    img = img.point(lambda p: p > threshold and 255) 

    # filter - noise
    img = img.filter(ImageFilter.MedianFilter(5)) 

    # pix = np.array(img)
    
    # otsuPix = otsu(pix)

    # img.putdata(otsuPix)

    # show
    img.show()
    
    # save
    img.save('output.jpg')

