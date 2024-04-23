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
            r, c = imgarray.shape
            imgarray = imgarray.tolist()
            
            p = int(input("Enter the value of p: "))  # Ask user for p
            q = int(input("Enter the value of q: "))  # Ask user for q
            
            n = p * q
            phi = (p - 1) * (q - 1)
            
            # No need to calculate d here, as it's calculated based on e and phi below
            
            print("Public key : ", e)
            
            d = 1
            while True:
                if ((d * e) - 1) % phi == 0 and d * e > 1:
                    break
                d += 1
            
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
