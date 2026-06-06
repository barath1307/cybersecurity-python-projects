import re

user_input = input("Enter text: ")

clean_text = re.sub(r'<.*?>', '', user_input)

print("\n===== INPUT SANITIZATION REPORT =====")
print("Original Input :", user_input)
print("Sanitized Input:", clean_text)