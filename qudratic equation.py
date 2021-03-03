from math import sqrt

a = int(input('Enter a\n'))
b = int(input('Enter b\n'))
c = int(input('Enter c\n'))
if a != 0 and b != 0 and c != 0:
    d = b**2-4*a*c
    if d > 0:
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        print ('x1 =',x1)
        print ('x2 =',x2)
    elif d == 0:
        x = (-b)/(2*a)
        print ('x = ' , x)
    else:
        print ('no roots')
elif a != 0 and b != 0 and c == 0:
    print ('x1 = 0')
    x2 = (-b)/a
    print ('x2 = ',x2)
elif a != 0 and b == 0 and c != 0:
    x = -c/a
    if x >= 0:
        x1 = sqrt(-c/a)
        x2 = -sqrt(-c/a)
        print ('x1 =',x1)
        print ('x2 =',x2)
    else:
        print ('no roots')    
else:
    print ('Error')
