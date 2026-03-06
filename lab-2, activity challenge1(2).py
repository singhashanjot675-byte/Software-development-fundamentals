# U Shape Area Program

# Assertion 1: If s=10, g=6, q=4, w=3 → area should be 48
# Assertion 2: If s=12, g=8, q=6, w=4 → area should be 72

s = float(input("Enter outer width (s): "))
g = float(input("Enter outer height (g): "))
q = float(input("Enter inner width (q): "))
w = float(input("Enter inner height (w): "))

area = (s * g) - (q * w)

print("Area =", area)