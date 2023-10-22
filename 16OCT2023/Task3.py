""""
Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""

side_a = int(input("Enter the length of side 'a' : \n"))
side_b = int(input("Enter the length of side 'b' : \n"))
side_c = int(input("Enter the length of side 'c' : \n"))

if side_a == side_b == side_c:
    print(f"This is a Equilateral triangle with 3 sides equal : {side_a},{side_b} and {side_c}")

elif side_a == side_b or side_a == side_c or side_b == side_c:
    print(f"This is a Isosceles tringle with 2 sides equal : {side_a},{side_b} and {side_c}")

elif side_a != side_b and side_a != side_c and side_b != side_c:
    print(f"This is a Scalene triangle with none of the sides equal  : {side_a},{side_b} and {side_c}")

else:
    print("This is non of the three triangles & is some another triangle")