import numpy as np
from PIL import Image

def encrypt_image(filename, key):
    try:
        img = Image.open(filename).convert('L') 
        imgarray = np.array(img)
        fname = 'EncryptedImage.jpeg'
        with open(fname, 'w+') as fobj:
            e, _d, n = key
            r, c = imgarray.shape
            imgarray = imgarray.tolist()

            fobj.write(str(r) + '^')
            fobj.write(str(c) + '^')

            for i in range(r):
                for j in range(c):
                    enc_value = (imgarray[i][j] ** e) % n
                    fobj.write(str(enc_value) + '^')

            print('Image encrypted as ', fname, '!')
            return fname

    except IOError:
        print('Image not found!')
        return None

def decrypt_image(filename, key):
    try:
        with open(filename, 'r') as fobj:
            data = fobj.read().split('^')  # Split the data
            _e, d, n = key
            r = int(data[0])
            c = int(data[1])
            # Filter out empty string elements and then convert the remaining to integers
            data = [int(x) for x in data[2:] if x.strip()]

            imgarray_decrypted = np.empty([r, c], dtype='int32')
            imgarray_decrypted = imgarray_decrypted.tolist()

            p = 0
            for i in range(r):
                for j in range(c):
                    imgarray_decrypted[i][j] = pow(data[p], d, n)  # Decryption
                    p += 1

            # Normalize values to range [0, 255]
            max_value = np.max(imgarray_decrypted)
            min_value = np.min(imgarray_decrypted)
            imgarray_decrypted = np.array(imgarray_decrypted)
            imgarray_decrypted = ((imgarray_decrypted - min_value) / (max_value - min_value)) * 255

            imgarray = np.array(imgarray_decrypted, dtype=np.uint8)  # Convert to uint8

            img = Image.fromarray(imgarray).convert('L')
            img.save("DecryptedImage.jpeg")
            print("Image Decrypted!")
            return "DecryptedImage.jpeg"

    except FileNotFoundError:
        print(f'File with name', filename, ' not found!')
        return None
