import requests

domain = input("Enter domain (without https://): ")

subdomains = [
    "www",
    "mail",
    "api",
    "blog",
    "dev",
    "test"
]

print("\n===== SUBDOMAIN REPORT =====\n")

for sub in subdomains:
    url = f"https://{sub}.{domain}"

    try:
        response = requests.get(url, timeout=3)

        print(f"[FOUND] {url} | {response.status_code}")

    except:
        print(f"[NOT FOUND] {url}")