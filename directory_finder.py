import requests

website = input("Enter Website URL: ")

paths = [
    "/admin",
    "/login",
    "/dashboard",
    "/uploads",
    "/images",
    "/api",
    "/config",
    "/backup",
    "/user",
    "/panel"
]

print("\nScanning...\n")

for path in paths:
    url = website + path

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
    if len(response.text) > 100:
        print(f"[FOUND] {url} | {response.status_code}")
    else:
        print(f"[POSSIBLE] {url} | {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"[ERROR] {url}")

print("\nScan Completed!")