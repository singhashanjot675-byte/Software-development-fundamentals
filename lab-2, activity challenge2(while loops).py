# Program to find the sum of the first n positive integers

n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print("Sum =", total)