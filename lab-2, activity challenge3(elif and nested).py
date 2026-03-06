# Vowel or Consonant Program

letter = input("Enter a letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter is a vowel.")
elif letter == "y":
    print("Sometimes y is a vowel and sometimes a consonant.")
else:
    print("The letter is a consonant.")


# Assertion Test Cases
# Test 1: If input = a → Output should be "The letter is a vowel."
# Test 2: If input = b → Output should be "The letter is a consonant."