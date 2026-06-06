import psutil

net = psutil.net_io_counters()

print("\n===== TRAFFIC REPORT =====")
print("Bytes Sent     :", net.bytes_sent)
print("Bytes Received :", net.bytes_recv)
print("Packets Sent   :", net.packets_sent)
print("Packets Recv   :", net.packets_recv)