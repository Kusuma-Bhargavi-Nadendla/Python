import math
class Triangle(object):
    def __init__(self,a,b,c):
        self.a=a 
        self.b=b 
        self.c=c 
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        return self.a+self.b+self.c 
class Square():
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4
class Rectangle():
    def __init__(self,l,b):
        self.a=l 
        self.b=b 
    def area(self):
        return self.a*self.b 
    def perimeter(self):
        return 2*(self.a+self.b)
class Circle():
    def __init__(self,r):
        self.r =r   
    def area(self):
        return math.pi*self.r*self.r 
    def perimeter(self):
        return 2*math.pi*self.r
print('Enter shape-')
s=input()
s=s.lower()
if s=='triangle':
    a,b,c=[int(x) for x in input('Enter sides-').split()]
    obj=Triangle(a,b,c)
    print('Area of triangle is :',obj.area())
    print('Perimeter of triangle is :',obj.perimeter())
elif s=='square':
    s=int(input('Enter side :'))
    obj=Square(s)
    print('Area of square is :',obj.area())
    print('Perimeter of square is :',obj.perimeter())
elif s=='circle':
    r=int(input('Enter radius :'))
    obj=Circle(r)
    print('Area of Circle is :%.2f'%(obj.area()))
    print('Perimeter of circle is :%.2f'%(obj.perimeter()))
elif s=='rectangle':
    l,b=[int(x) for x in input('Enter sides:').split()]
    obj=Rectangle(l,b)
    print('Area of rectangle is :',obj.area())
    print('Perimeter of rectangle is :',obj.perimeter())
else:
    print('Shape not found')
