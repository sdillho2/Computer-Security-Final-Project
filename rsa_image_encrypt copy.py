import random


if __name__=="__main__":
    from PIL import Image
    import numpy
    imgname=input('Enter image name: ')
    try:
        img=Image.open(imgname).convert('L') 
        imgarray=numpy.array(img)
        fname=input('Enter destination encrypted file name: ')
        with open(fname,'w') as fobj:
            e=1
            r,c=imgarray.shape
            imgarray=imgarray.tolist()
            n = int(input('Enter n: '))
            d = int(input('Enter private key (d): '))
            e = int(input('Enter public key (e): '))
            fobj.write(str(r)+'^')
            fobj.write(str(c)+'^')
            for i in range(r):
                for j in range(c):
                    enc_value=(imgarray[i][j]**e)%n
                    fobj.write(str(enc_value)+'^')
            #print(f'Image encrypted as {fname}!!')
            print('Image encrypted as ',fname,'!')
    except IOError:
        print('Image not found!')



