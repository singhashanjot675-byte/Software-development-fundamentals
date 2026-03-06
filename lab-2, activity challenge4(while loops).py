# Password Program

password = "python123"
attempts = 0

while attempts < 3:
    user = input("Enter password (or type exit to quit): ")

    if user == "exit":
        print("Program terminated.")
        break

    if user == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password.")
        attempts = attempts + 1

if attempts == 3:
    print("Too many attempts. Access denied.")