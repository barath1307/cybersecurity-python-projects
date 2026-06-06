import shutil

source = input("Enter source file name: ")
destination = input("Enter backup file name: ")

try:
    shutil.copy(source, destination)

    print("\n===== BACKUP REPORT =====")
    print("Source      :", source)
    print("Backup File :", destination)
    print("Backup Created Successfully!")

except FileNotFoundError:
    print("Source file not found!")