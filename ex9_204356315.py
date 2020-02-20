###########################################
# Question 1 - do not delete this comment #
###########################################

class Matrix:
    def __init__(self,lst):
        self.lst=lst[:]
        length=len(lst[0]) #columns, assuming matrix has 1 line and 1 column at least
        for i in range(1,len(lst)):
            if len(lst[i])!=length:
                raise ValueError('not all lines are of same length')
        self.dim=(len(lst),length)

    def __repr__(self):
        return str(self.lst)

    def get(self,i,j): #i-line , j-column
        if i>=self.dim[0] or j>=self.dim[1]:
            raise IndexError('matrix index out of range')
        return self.lst[i][j]

    def transpose(self):
        tran=[]
        for j in range(0,self.dim[1]):
            temp_list=[]
            for i in range(0,self.dim[0]): #scanning by columns
                temp_list.append(self.get(i,j))
            tran.append(temp_list)
        return Matrix(tran)

    def __add__(self,other):
        if self.dim[0]!=other.dim[0] or self.dim[1]!=other.dim[1]:
            raise ValueError('dims do not match')
        sum_mat=[]
        for i in range(0,self.dim[0]):
            temp_list=[]
            for j in range(0,self.dim[1]):
                temp_list.append(self.get(i,j)+other.get(i,j))
            sum_mat.append(temp_list)
        return Matrix(sum_mat)

    def __mul__(self,other):
        if self.dim[0]!=other.dim[0] or self.dim[1]!=other.dim[1]:
            raise ValueError('dims do not match')
        mul_mat=[]
        for i in range(0,self.dim[0]):
            temp_list=[]
            for j in range(0,self.dim[1]):
                temp_list.append(self.get(i,j)*other.get(i,j))
            mul_mat.append(temp_list)
        return Matrix(mul_mat)

    def dot(self,other):
        if self.dim[1]!=other.dim[0]:
            raise ValueError('dims do not match')
        m=self.dim[0]
        n1=self.dim[1]
        n2=other.dim[0]
        p=other.dim[1]
        mat=[]
        value=0
        for i in range(0,m):
            temp_mat=[]
            for j in range(0,p):
                    for k in range(0,n1):
                            value+=self.get(i,k)*other.get(k,j)
                    temp_mat.append(value)
                    value=0
            mat.append(temp_mat)
        return Matrix(mat)


###########################################
# Question 2 - do not delete this comment #
###########################################

######### do not edit this class ##########
class Point: 
    def __init__(self,x,y):
        ''' x and y are int or float '''
        self.x = x
        self.y = y
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def shift(self,dx,dy):
        self.x += dx
        self.y += dy
###########################################
        

class Polygon:
    def __init__(self,points): #points is a tuple of Point obejects
        if len(points)<3:
            raise ValueError('not enough vertices')
        else:   self.vertices=points   

    def __repr__(self):
        return str(self.vertices)

    def shift(self,dx,dy):
        for point in self.vertices:
            point.shift(dx,dy)

    def circumference(self):
        length=len(self.vertices)
        circ=self.vertices[length-1].distance(self.vertices[0]) #last point with 1st point
        for i in range(0,length-1):
            circ+=self.vertices[i].distance(self.vertices[i+1])
        return circ    

class Square(Polygon):
    def __init__(self,points):
        if len(points)!=4:
            raise ValueError("the given vertices don't form a square")
        edge=points[len(points)-1].distance(points[0]) #last vertice
        valid=True
        for i in range(0,len(points)-1): #all vertices are equal
            if edge!=points[i].distance(points[i+1]):
                valid=False
        ##diagonals are equal
        if points[0].distance(points[2])!=points[1].distance(points[3]) and not valid:
            raise ValueError("the given vertices don't form a square")
        self.edge=edge
        self.vertices=points 

    def __repr__(self):
        return 'Square - ' + Polygon.__repr__(self)

    def circumference(self):
        return self.edge*4

    def area(self):
        return self.edge*self.edge

        
class Triangle(Polygon):
    def __init__(self,points):
        if len(points)!=3:
            raise ValueError("triangle must have 3 vertices")
        self.vertices=points

    def __repr__(self):
        return 'Triangle - ' + Polygon.__repr__(self)

    def area(self):
        s=self.circumference()/2.0
        a=self.vertices[0].distance(self.vertices[1])
        b=self.vertices[1].distance(self.vertices[2])
        c=self.vertices[2].distance(self.vertices[0])
        return (s*(s-a)*(s-b)*(s-c))**0.5
