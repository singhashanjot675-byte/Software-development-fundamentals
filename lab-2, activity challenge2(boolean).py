# Webstore Purchase Checker

# Assertion 1:
# registered = yes, items = 2, guest = no
# Expected output: Purchase allowed

# Assertion 2:
# registered = no, items = 0, guest = yes
# Expected output: Purchase allowed (guest buying gift card)

registered = input("Are you registered? (yes/no): ")
items = int(input("How many items are in your cart?: "))
guest = input("Are you using guest checkout? (yes/no): ")

# Check conditions
if (registered == "yes" and items > 0) or (guest == "yes"):
    print("Purchase allowed")
else:
    print("Purchase not allowed")