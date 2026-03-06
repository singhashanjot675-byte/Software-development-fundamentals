# Richter Scale Program

magnitude = float(input("Enter earthquake magnitude: "))

if magnitude < 2.0:
    print("This is a Micro earthquake.")
elif magnitude < 3.0:
    print("This is a Very minor earthquake.")
elif magnitude < 4.0:
    print("This is a Minor earthquake.")
elif magnitude < 5.0:
    print("This is a Light earthquake.")
elif magnitude < 6.0:
    print("This is a Moderate earthquake.")
elif magnitude < 7.0:
    print("This is a Strong earthquake.")
elif magnitude < 8.0:
    print("This is a Major earthquake.")
elif magnitude < 10.0:
    print("This is a Great earthquake.")
else:
    print("This is a Meteoric earthquake.")

# Assertion Test Cases
# Test 1: If input = 5.5 → Output should say "Moderate earthquake"
# Test 2: If input = 7.2 → Output should say "Major earthquake"