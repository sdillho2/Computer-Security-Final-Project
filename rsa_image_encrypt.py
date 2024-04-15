import random

def prime(start, stop): #Returns a random prime number between start and stop
    pno=[]
    for i in range(start,stop):
        isPrime=True
        for j in range(2,i):
            if(i%j==0):
                isPrime=False
                break
        if(isPrime):
            pno.append(i)
    l=len(pno)
    return pno[random.randint(0,l-1)]

def hcf(a,b):     #Returns HCF of two numbers
    while(b!=0):
        c=a%b
        if(c==0):
            return b
        else:
            a=b
            b=c



if __name__=="__main__":
    from PIL import Image
    import numpy
    imgname=input('Enter image name: ')
    try:
        img=Image.open(imgname).convert('L') 
        imgarray=numpy.array(img)
        fname=input('Enter destination encrypted file name: ')
        with open(fname,'w+') as fobj:
            e=1
            r,c=imgarray.shape
            imgarray=imgarray.tolist()
            p,q=prime(2,100),prime(101,200)
            print("p =",p,"\b\tq = ",q)
            n=p*q
            phi=(p-1)*(q-1)
            for e in range(2,phi):
                gcd=hcf(e,phi)
                if(gcd==1):
                    print()
                    break
            print("Public key : ",e)
            d=1
            while(True):
                 if ((d*e)-1)%phi==0 and d*e>1:
                     break
                 d+=1
            print("Private key = ",d)
            print("n = ",n)
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



