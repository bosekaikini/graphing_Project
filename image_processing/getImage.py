import cv2
import numpy as np

#Goal: Take an image and convert it to a usable matrix

def get_image(image_path):

#load in with grayscale
    img=cv2.imread(image_path, 0)

#finding points(estimated points)

#here is where ml model 1 will be helpful
    points=np.where(img < 10, 1, 0)

    height,width=points.shape

    ys,xs=(points==1).nonzero()
    
#get the x and y values of all points
    x=xs.astype(float)
    y=(height-1-ys).astype(float)

#ensure uniqueness

    return x,y
