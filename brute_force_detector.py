filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    failed_attempts = 0

    for line in lines:
        if "failed" in line.lower():
            failed_attempts += 1

    print("\n===== BRUTE FORCE REPORT =====")
    print("Failed Attempts:", failed_attempts)

    if failed_attempts >= 5:
        print("⚠ Possible Brute Force Attack Detected!")
    else:
        print("✓ No Brute Force Attack Detected")

except FileNotFoundError:
    print("Log file not found!")