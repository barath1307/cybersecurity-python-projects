import requests

url = input("Enter Website URL: ")

try:
    response = requests.get(url, allow_redirects=True)
    print("\nFinal URL:", response.url)
print("Status Code:", response.status_code)

    headers = {
    "Strict-Transport-Security": "HTTPS protection",
    "Content-Security-Policy": "XSS protection",
    "X-Frame-Options": "Clickjacking protection",
    "X-Content-Type-Options": "MIME sniffing protection"
}

for header, purpose in headers.items():
    if header in response.headers:
        print(f"[FOUND] {header} - {purpose}")
    else:
        print(f"[MISSING] {header} - {purpose}")

except requests.exceptions.RequestException:
    print("Connection Error")