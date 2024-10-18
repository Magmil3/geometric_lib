
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

Below are ways to work with these files and the functions they contain



## File circle.py
Contains two functions:

1. area(r) - takes the number r - the radius of the circle, returns the area of ​​the circle
- Example call:

'''python
from circle import area
circleArea = area(2)
print(circleArea) #4pi
'''

2. perimetr(r) - takes the number r - the radius of the circle, returns the circumference
- Example call:

'''python
from circle import area
circleArea = perimeter(2)
print(circlePerimetr) #4pi
'''

## File triangle.py
Contains two functions:

1. area(a,b,c) - accepts the numbers a,b,c - the lengths of the sides of the triangle, returns the semi-perimeter of the triangle
- Example call:

'''python
from triangle import area
triangleArea = area(5, 7, 11)
print(triangleArea) #11,5
'''

2. perimeter(a,b,c) - accepts the numbers a,b,c - the lengths of the sides of the triangle, returns the perimeter of the triangle
- Example call:

'''python
from triangle import perimeter
trianglePerimeter = perimeter(5, 7, 11)
print(trianglePerimetr) #23
'''

## File rectangle.py
Contains two functions:

1. area(a,b) - takes the numbers a,b - the lengths of the sides of the rectangle, returns the area of ​​the rectangle
- Example call:

'''python
from rectangle import area
rectangleArea = area(5, 7)
print(circleArea) #35
'''

2. perimeter(a, b) - accepts the numbers a,b - the lengths of the sides of the rectangle, returns the perimeter
- Example call:

'''python
from rectangle import perimetr
rectanglePerimetr = perimeter(5, 7)
print(rectanglePerimetr) #24
'''

## File square.py
Contains two functions:

1. area(a) - takes the number a - the length of the side of the square, returns the area of ​​the square
- Example call:

'''python
from square import area
squareArea = area(5)
print(circleArea) #25
'''

2. perimeter(a) - takes the number a - the length of the side of the square, returns the perimeter
- Example call:

'''python
from circle import area
rectanglePerimetr = perimeter(5)
print(rectanglePerimetr) #20
'''

b5b0fae (origin/develop, develop) L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added