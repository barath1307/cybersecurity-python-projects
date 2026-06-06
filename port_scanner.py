import socket

target = input("Enter IP address or domain: ")

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

print("\n===== PORT SCAN REPORT =====\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")

    sock.close()