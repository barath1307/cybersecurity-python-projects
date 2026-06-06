filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        content = file.readlines()

    errors = 0
    warnings = 0
    infos = 0

    for line in content:
        if "ERROR" in line:
            errors += 1
        elif "WARNING" in line:
            warnings += 1
        elif "INFO" in line:
            infos += 1

    print("\n===== LOG FILE REPORT =====")
    print("Errors  :", errors)
    print("Warnings:", warnings)
    print("Infos   :", infos)

except FileNotFoundError:
    print("Log file not found!")