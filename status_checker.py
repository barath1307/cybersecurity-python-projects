import requests
import time

url = input("Enter Website URL: ")

try:
    start_time = time.time()

    response = requests.get(url, timeout=10)

    end_time = time.time()

    response_time = round(end_time - start_time, 2)

    print("\n========== WEBSITE REPORT ==========")
    print("Website       :", url)
    print("Status Code   :", response.status_code)
    print("Status Message:", response.reason)

    if response.status_code == 200:
        print("Website Status: UP")
    else:
        print("Website Status: DOWN")

    print("Response Time :", response_time, "seconds")
    print("Server        :", response.headers.get("Server", "Unknown"))
    print("====================================")

except requests.exceptions.RequestException as e:
    print("\nConnection Error!")
    print(e)