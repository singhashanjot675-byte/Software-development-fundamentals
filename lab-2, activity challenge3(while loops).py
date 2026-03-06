# Program to print multiples of p from 10 up to q

p = int(input("Enter p: "))
q = int(input("Enter q: "))

i = 10

while i <= q:
    if i % p == 0:
        print(i, end=", ")
    i = i + 1