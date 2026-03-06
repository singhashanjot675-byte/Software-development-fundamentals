# Arrow Shape Area Program

# Assertion 1: If m=6, u=4, n=4 → area should be 32
# Assertion 2: If m=10, u=5, n=6 → area should be 65

m = float(input("Enter rectangle length (m): "))
u = float(input("Enter height (u): "))
n = float(input("Enter triangle length (n): "))

rectangle = m * u
triangle = (u * n) / 2

area = rectangle + triangle

print("Area =", area)