import ssl
import socket

hostname = input("Enter website domain: ")

try:
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:

            cert = ssock.getpeercert()

            print("\n===== SSL CERTIFICATE REPORT =====")
            print("Subject :", cert.get('subject'))
            print("Issuer  :", cert.get('issuer'))
            print("Expires :", cert.get('notAfter'))

except Exception as e:
    print("Error:", e)