# Chinese Zodiac Program

year = int(input("Enter a year: "))

z = year % 12

if z == 8:
    print("Dragon")
elif z == 9:
    print("Snake")
elif z == 10:
    print("Horse")
elif z == 11:
    print("Sheep")
elif z == 0:
    print("Monkey")
elif z == 1:
    print("Rooster")
elif z == 2:
    print("Dog")
elif z == 3:
    print("Pig")
elif z == 4:
    print("Rat")
elif z == 5:
    print("Ox")
elif z == 6:
    print("Tiger")
elif z == 7:
    print("Hare")

# Assertion Test Cases
# Test 1: If input = 2000 → Output should be "Dragon"
# Test 2: If input = 2010 → Output should be "Tiger"