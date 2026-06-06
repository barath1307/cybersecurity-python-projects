patterns = [
    "' OR '1'='1",
    '" OR "1"="1',
    "UNION SELECT",
    "DROP TABLE",
    "--",
    ";"
]

user_input = input("Enter SQL Query or Input: ")

found = False

for pattern in patterns:
    if pattern.lower() in user_input.lower():
        found = True
        break

print("\n===== SQL INJECTION REPORT =====")

if found:
    print("⚠ Potential SQL Injection Detected!")
else:
    print("✓ No SQL Injection Pattern Found")