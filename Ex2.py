import math
print("the quadratic equation form is : ax^2 + bx + c")

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))


underRadical = (b**2) - (4*a*c)

if underRadical >= 0: 
    x1 = -b +  math.sqrt(underRadical) / (2 * a)

    x2 = -b -  math.sqrt(underRadical) / (2 * a)

    print('x1: ', x1 , 'x2: ', x2)
else:
    print('no answer')