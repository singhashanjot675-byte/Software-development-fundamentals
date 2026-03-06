import math

# Assertion 1: If e = 6, g = 4, f = 8 → area ≈ 30.14
# Assertion 2: If e = 8, g = 5, f = 10 → area ≈ 45.13

e = float(input("Enter diameter (e): "))
g = float(input("Enter height (g): "))
f = float(input("Enter triangle base (f): "))

r = e / 2

half_circle = (math.pi * r * r) / 2
triangle = (f * g) / 2

area = half_circle + triangle

print("Area =", area)