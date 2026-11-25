import os
import platform
import shutil
import socket

def check_port(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1.0)
        return sock.connect_ex((host, port)) == 0

def run_audit() -> None:
    total, used, free = shutil.disk_usage("/")
    print(f"Host: {platform.node()} ({platform.system()} {platform.release()})")
    print(f"Disk Free: {free // (1024**3)} GB / {total // (1024**3)} GB")
    if hasattr(os, "getloadavg"):
        print(f"Load Average (1m, 5m, 15m): {os.getloadavg()}")
    for port in (22, 80, 443):
        status = "OPEN" if check_port("127.0.0.1", port) else "CLOSED"
        print(f"Local Port {port}: {status}")

if __name__ == "__main__":
    run_audit()
