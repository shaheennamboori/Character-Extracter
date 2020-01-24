
Convert pil image object to numpy array:
```python
pix = numpy.array(pic)
```

Convert numpy array to pillow pic
```python
pic.putdata(pix)
# or create new img
Image.fromarray(pix)
```

dialation and errosion
```python
dilation_img = src_img.filter(ImageFilter.MaxFilter(3))
erosion_img = src_img.filter(ImageFilter.MinFilter(3))
```

otsu thresholding

```python
def otsu(gray):
    pixel_number = gray.shape[0] * gray.shape[1]
    mean_weigth = 1.0/pixel_number
    his, bins = np.histogram(gray, np.array(range(0, 256)))
    final_thresh = -1
    final_value = -1
    for t in bins[1:-1]: # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
        Wb = np.sum(his[:t]) * mean_weigth
        Wf = np.sum(his[t:]) * mean_weigth

        mub = np.mean(his[:t])
        muf = np.mean(his[t:])

        value = Wb * Wf * (mub - muf) ** 2

        # print("Wb", Wb, "Wf", Wf)
        # print("t", t, "value", value)

        if value > final_value:
            final_thresh = t
            final_value = value
    final_img = gray.copy()
    # print(final_thresh)
    final_img[gray > final_thresh] = 255
    final_img[gray < final_thresh] = 0
    return final_img
```

[convert image to segments](https://stackoverflow.com/questions/10964226/how-to-convert-an-image-into-character-segments)