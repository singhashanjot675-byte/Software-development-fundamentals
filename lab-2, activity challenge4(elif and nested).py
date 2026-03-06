# Performance Review Program

rating = float(input("Enter employee rating: "))

if rating == 0.0:
    bonus = 2400 * rating
    print("Unacceptable performance")
    print("Bonus = $", bonus)

elif rating == 0.4:
    bonus = 2400 * rating
    print("Acceptable performance")
    print("Bonus = $", bonus)

elif rating >= 0.6:
    bonus = 2400 * rating
    print("Meritorious performance")
    print("Bonus = $", bonus)

else:
    print("Error: Invalid rating entered")


# Assertion Test Cases
# Test 1: If input = 0.4 → Output: Acceptable performance, Bonus = $960
# Test 2: If input = 0.6 → Output: Meritorious performance, Bonus = $1440