class Point():
    def __init__(self,x,y):
        self.x=x 
        self.y=y  
    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)
    def __add__(self,other):
        x=self.x+other.x 
        y=self.y+other.y  
        return Point(x,y)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Point(x,y)
    def __mul__(self,other):
        x=self.x*other.x 
        y=self.y*other.y 
        return Point(x,y)
    def __gt__(self,other):
        return (self.x,self.y)>(self.y,other.y)
x1,y1=[int(x) for x in input('Point 1:').split()]
x2,y2=[int (x) for x in input('Point 2:').split()]
p1=Point(x1,y1)
p2=Point(x2,y2)
print('Sum-',p1+p2)
print('Difference-',p1-p2)
print('Product-',p1*p2)
print('Greater-',p1>p2)


