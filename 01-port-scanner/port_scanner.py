import socket

def scan_ports(target, ports):
    print(f"[+] Scanning target: {target}")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = [22, 80, 443]
    scan_ports(target, ports)
