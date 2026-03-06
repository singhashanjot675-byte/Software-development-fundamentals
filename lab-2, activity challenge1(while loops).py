# Print numbers from 1 to n in square brackets

n = int(input("Enter a number: "))

i = 1

while i <= n:
    print("[" + str(i) + "]", end=" ")
    i = i + 1