# Matrix class tests:
A = Matrix([[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2, 8]])
assert A.lst == [[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2, 8]]
assert A.dim == (4, 3)
assert A.get(2, 1) == 5
B = A.transpose()
assert A.lst == [[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2, 8]]
assert B.lst == [[1, 3, 4, 0], [0, 1, 5, 2], [2, 1, 2, 8]]
assert B.dim == (3, 4)
C = Matrix([[1, 3, 4], [0, 1, 5], [2, 1, 2], [4, 6, 8]])
D = A + C
assert A.lst == [[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2, 8]]
assert C.lst == [[1, 3, 4], [0, 1, 5], [2, 1, 2], [4, 6, 8]]
assert D.lst == [[2, 3, 6], [3, 2, 6], [6, 6, 4], [4, 8, 16]]
E = A * C
assert A.lst == [[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2, 8]]
assert C.lst == [[1, 3, 4], [0, 1, 5], [2, 1, 2], [4, 6, 8]]
assert E.lst == [[1, 0, 8], [0, 1, 5], [8, 5, 4], [0, 12, 64]]
F = A.dot(B)
assert A.lst == [[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2, 8]]
assert B.lst == [[1, 3, 4, 0], [0, 1, 5, 2], [2, 1, 2, 8]]
assert F.lst == [[5, 5, 8, 16], [5, 11, 19, 10], [8, 19, 45, 26], [16, 10, 26, 68]]
try:
    a = Matrix([[1, 0, 2], [3, 1, 1], [4, 5, 2], [0, 2]])
    raise AssertionError
except ValueError:
    pass
try:
    A.get(2, 3)
    raise AssertionError
except IndexError:
    pass
try:
    A * B
    raise AssertionError
except ValueError:
    pass
try:
    A.dot(C)
    raise AssertionError
except ValueError:
    pass

# Polygon class tests:
a = Point(0, 0)
b = Point(0, 2)
c = Point(2, 2)
d = Point(2, 0)
e = Point(1, -1)
try:
    P = Polygon((a, b))
    raise AssertionError
except ValueError:
    pass
P = Polygon((a, b, c, d, e))
assert str(P) == "((0, 0), (0, 2), (2, 2), (2, 0), (1, -1))"
P.shift(1, 0)
P.shift(0.5, -1)
assert str(P) == "((1.5, -1), (1.5, 1), (3.5, 1), (3.5, -1), (2.5, -2))"
assert P.circumference() == 8.82842712474619

# Square class tests:
a = Point(0, 0)
b = Point(0, 2)
c = Point(2, 2)
d = Point(2, 0)
e = Point(-1, -1)
try:
    S = Square((a, b, c))
    raise AssertionError
except ValueError:
    pass
try:
    S = Square((b, c, d, e))
    raise AssertionError
except ValueError:
    pass
S = Square((a, b, c, d))
assert str(S) == "Square - ((0, 0), (0, 2), (2, 2), (2, 0))"
S.shift(2, 2)
assert str(S) == "Square - ((2, 2), (2, 4), (4, 4), (4, 2))"
assert S.circumference() == 8.0
assert S.area() == 4.0

# Triangle class tests:
a = Point(0, 0)
b = Point(0, 2)
c = Point(2, 2)
try:
    T = Triangle((a, b, c, d))
    raise AssertionError
except ValueError:
    pass
T = Triangle((a, b, c))
assert str(T) == "Triangle - ((0, 0), (0, 2), (2, 2))"
T.shift(-1, -1)
assert str(T) == "Triangle - ((-1, -1), (-1, 1), (1, 1))"
assert T.circumference() == 6.82842712474619
assert T.area() == 1.9999999999999993

print "all preliminary tests were completed! good job!"