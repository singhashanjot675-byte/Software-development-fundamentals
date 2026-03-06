import math

# Assertion 1: If e = 6 and g = 4 → area ≈ 22.43
# Assertion 2: If e = 8 and g = 5 → area ≈ 36.56

e = float(input("Enter diameter (e): "))
g = float(input("Enter height (g): "))
angle = 38

r = e / 2

half_circle = (math.pi * r * r) / 2

triangle_base = g / math.tan(math.radians(angle))
triangle = (triangle_base * g) / 2

area = half_circle + triangle

print("Area =", area)