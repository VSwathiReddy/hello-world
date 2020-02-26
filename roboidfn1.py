import cv2
import numpy as np
#from cv2 import cv

#method = cv.CV_TM_SQDIFF_NORMED

# Read the images from the file
med_image = cv2.imread('heart.jpg')
large_image = cv2.imread('image1.jpg')

result = cv2.matchTemplate(med_image, large_image, cv2.TM_SQDIFF_NORMED)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = med_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

# The image is only displayed if we call this
cv2.waitKey(4000)

print('Heart Identified')

# Read the images from the file
small_image = cv2.imread('tumor.jpg')
#large_image = cv2.imread('anthracnose.jpg')

result = cv2.matchTemplate(small_image, large_image, cv2.TM_SQDIFF_NORMED)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

print('Tumor Identified')

# The image is only displayed if we call this
cv2.waitKey(4000)


