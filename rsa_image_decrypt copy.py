import numpy as np
from PIL import Image

fname = input("Enter encrypted file name: ")
imgname = input("Enter decrypted destination image name: ")

try:
    with open(fname, 'r') as fobj:
        l = fobj.read().split('^')
        p = 0
        d = int(input("Enter private key (d): "))
        n = int(input("Enter n: "))
        r = int(l[0])
        c = int(l[1])
        l = l[2:]
        
        imgarray_decrypted = np.empty([r, c], dtype='int32')
        imgarray_decrypted = imgarray_decrypted.tolist()
        
        for i in range(r):
            for j in range(c):
                imgarray_decrypted[i][j] = pow(int(l[p]), d, n)
                p = p + 1
        
        imgarray = np.array(imgarray_decrypted, dtype=np.uint8)  # Convert to uint8
        
        img = Image.fromarray(imgarray).convert('L')
        img.save(imgname)
        print("Image Decrypted!")
        
except FileNotFoundError:
    print(f'File with name', fname, ' not found!') 
