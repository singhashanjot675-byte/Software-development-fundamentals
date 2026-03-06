import math

# Assertion 1: If c = 4, area ≈ 37.70
# Assertion 2: If c = 6, area ≈ 84.82

c = float(input("Enter radius (c): "))

circle = math.pi * c * c

area = (3/4) * circle

print("Area =", area)