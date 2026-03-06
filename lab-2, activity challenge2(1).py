import math

# Assertion 1: If x = 6 and y = 10, area should be about 74.27
# Assertion 2: If x = 4 and y = 8, area should be about 41.13

x = float(input("Enter height (x): "))
y = float(input("Enter length (y): "))

r = x / 2

rectangle = x * y
half_circle = (math.pi * r * r) / 2

area = rectangle + half_circle - half_circle

print("Area =", area)