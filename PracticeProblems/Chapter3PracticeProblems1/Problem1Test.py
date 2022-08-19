import math

a1 = 0
b1 = 3
a2 = 2
b2 = 4

eps = 0.5

area = (a1 - b1)*(a2 - b2)

A = (a1 - b1) + (a2 - b2)
x = (1/4)*(A + math.sqrt(A**2 + 4*eps))

area2 = (a1 - b1 - 2*x)*(a2 - b2 - 2*x)

print(area)
print(area2)
print(area2 - area)