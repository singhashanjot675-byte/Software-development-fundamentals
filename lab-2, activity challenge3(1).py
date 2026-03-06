import math

# Assertion 1: If d = 6 and e = 10, area should be 24
# Assertion 2: If d = 5 and e = 13, area should be 30

d = float(input("Enter base (d): "))
e = float(input("Enter hypotenuse (e): "))

height = math.sqrt(e**2 - d**2)

area = (d * height) / 2

print("Area =", area)