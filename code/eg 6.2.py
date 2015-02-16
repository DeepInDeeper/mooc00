# applyfuction

def applyarea(a,f):
    '''assumes a is a list, f a function'''
    for i in range(len(a)):
        a[i]=f(a[i])

        

a=[1,2,3,4]
 
def circle_area(n):
    pi = 3.1415926
    return 2*pi*n
def square_area(n):
    return n*n
def ball_area(n):
    pi =3.1415
    return 4*pi*n**2

applyarea(a,circle_area)
print("the cirle area is "+str(a))
applyarea(a,square_area)
print(a)
    
