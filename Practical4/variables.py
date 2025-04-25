a,b=15,75
c=a+b #calculate the total time for bus-based transportation
d,e=90,5
f=d+e #calculate the total time for car-based transportation
if c>f:
    print('car-based transportation is faster than bus-based transportation')
elif c<f:
    print('bus-based transportation is faster than car-based transportation')
else:
    print('bus-based transportation is as fast as car-based transportarion')

 
X=True
Y=False 
W=X and Y
print(W)
#X=True and Y=False, so W=False
#X=True or Y=True, so W=True
#X=False and Y=False, so W=False
#X=False or Y=False, so W=False


