a,b=15,75
c=a+b #calculate the total time for bus-based transportation
d,e=90,5
f=d+e #calculate the total time for car-based transportation
if c>f:
    print('bus-based transportation is faster than car-based transportation')
elif c<f:
    print('car-based transportation is faster than bus-based transportation')
else:
    print('bus-based transportation is as fast as car-based transportarion')