if __name__=="__main__":
    from PIL import Image
    import numpy
    
    imgname = input('Enter image name: ')
    try:
        img = Image.open(imgname).convert('L') 
        imgarray = numpy.array(img)
        fname = input('Enter destination encrypted file name: ')
        with open(fname, 'w+') as fobj:
            e = int(input("Enter the value of e: "))  # Ask user for e
            d = int(input("Enter the value of d: "))  # Ask user for d
            n = int(input("Enter the value of n: "))  # Ask user for n
            
            r, c = imgarray.shape
            imgarray = imgarray.tolist()
            
            print("Public key : ", e)
            print("Private key = ", d)
            print("n = ", n)
            
            fobj.write(str(r) + '^')
            fobj.write(str(c) + '^')
            
            for i in range(r):
                for j in range(c):
                    enc_value = (imgarray[i][j] ** e) % n
                    fobj.write(str(enc_value) + '^')
            
            print('Image encrypted as ', fname, '!')
    
    except IOError:
        print('Image not found!')
