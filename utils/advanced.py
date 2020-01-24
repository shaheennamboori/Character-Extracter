from PIL import Image
import numpy as np
# from scipy import ndimage
import cv2 
import os

def _openImage(im):
    return cv2.imread(im)

def processImage(im):

    img = _openImage(im)

    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # smooth the image to avoid noises
    gray = cv2.medianBlur(gray,5)

    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # smooth the image to avoid noises
    gray = cv2.medianBlur(gray,3)



    # Apply adaptive threshold
    ret,thresh = cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)
    # thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)
    thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)

    # apply some dilation and erosion to join the gaps
    thresh = cv2.dilate(thresh,None,iterations = 3)
    thresh = cv2.erode(thresh,None,iterations = 2)

    # Find the contours
    # RETR_EXTERNAL only external contours
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # For each contour, find the bounding rectangle and draw it
    # Create folder if it doesnt exist
    os.makedirs("output", exist_ok=True)
    i = 0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        # crop and save
        crop_img = thresh_color[y:y+h, x:x+w]
        if(w>=100 and h >= 100):
            cv2.imwrite("output/"+str(i)+".jpg", crop_img)
            i+=1
        #Add Recty
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(thresh_color, str(w)+","+str(h), (x, y), cv2.FONT_HERSHEY_SIMPLEX , 2, (0,255, 0),3 )

    # Finally show the image
    # cv2.imshow('img',img)
    cv2.imwrite('output.jpg', img)
    cv2.imwrite('output_thresh.jpg',thresh_color)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # histogram
    # hist, bin_edges = np.histogram(pix, bins=60)
    # bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

    # print("log",hist,bin_centers)
    


    # show
    # img.show()
    
    # save
    # img.save('output.jpg')

