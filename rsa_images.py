import cv2 as cv 
import numpy as np
import png
import imageio 
import time
from tqdm import tqdm 

start = time.time()

img = cv.imread('images.jpeg', 0)
#print(type(img))
img = img.astype(np.uint16)
a,b = img.shape
print('\n\nOriginal image: ')
print(img)
print((a,b))
tup = a,b

for i in tqdm(range(0, tup[0])):
	for j in tqdm(range(0, tup[1])):
		x = img[i][j] 
		x = (pow(x,3)%25777)
		img[i][j] = x

print('\n\nEncrypted Image:\n\n')
print(img)
#cv.imshow('EnImage', img)
cv.imwrite('EnImg.png', img)

end = time.time()
eTime = end - start

print(eTime)