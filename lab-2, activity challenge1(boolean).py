# Grammar School Enrolment Checker

# Assertion 1:
# distance = 3, age = 16, visa = yes, international = no
# Expected output: Student CAN enrol

# Assertion 2:
# distance = 10, age = 17, visa = no, international = yes
# Expected output: Student CAN enrol (international student)

distance = float(input("Enter distance from school in km: "))
age = int(input("Enter student age: "))
visa = input("Does the student have the right to stay in NZ? (yes/no): ")
international = input("Will the student pay international fees? (yes/no): ")

# Check conditions
if (distance < 4 and age < 18 and visa == "yes") or (age < 18 and international == "yes"):
    print("Student CAN enrol")
else:
    print("Student CANNOT enrol")