# Sound Level Program

db = int(input("Enter sound level in decibels: "))

if db == 130:
    print("Jackhammer")
elif db == 106:
    print("Petrol lawnmower")
elif db == 70:
    print("Alarm clock")
elif db == 40:
    print("Quiet room")

elif db > 106 and db < 130:
    print("Between Petrol lawnmower and Jackhammer")
elif db > 70 and db < 106:
    print("Between Alarm clock and Petrol lawnmower")
elif db > 40 and db < 70:
    print("Between Quiet room and Alarm clock")

elif db < 40:
    print("Quieter than a quiet room")
else:
    print("Louder than a jackhammer")


# Assertion Test Cases
# Test 1: If input = 70 → Output should be "Alarm clock"
# Test 2: If input = 80 → Output should be "Between Alarm clock and Petrol lawnmower"