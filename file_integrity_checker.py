import hashlib

filename = input("Enter file name: ")

try:
    with open(filename, "rb") as file:
        data = file.read()

    sha256_hash = hashlib.sha256(data).hexdigest()

    print("\n===== FILE INTEGRITY REPORT =====")
    print("File:", filename)
    print("SHA256:", sha256_hash)

except FileNotFoundError:
    print("File not found!")