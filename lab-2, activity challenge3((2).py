import math

# Assertion 1: If f = 10, area ≈ 41.95
# Assertion 2: If f = 6, area ≈ 15.10

f = float(input("Enter base (f): "))
angle = 40

height = math.tan(math.radians(angle)) * f

area = (f * height) / 2

print("Area =", area)