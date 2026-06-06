import re

password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1

# Number Check
if re.search(r"\d", password):
    score += 1

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\n===== PASSWORD STRENGTH REPORT =====")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")

print("Score:", score, "/ 5")