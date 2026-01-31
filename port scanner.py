import socket
host = ""#add your host here
ports = [80 , 443,22,21,20,3389,53]#add more ports if needed 

def scan_ports(host, port):
    try:
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#if ipv6 use AF_INET6
     sock.settimeout(5)#timeout for 5 seconds
     result = sock.connect_ex((host, port))#connect_ex return 0 if port is open
     sock.close()
     if result ==0:
         return True
     else:
         return False
    except Exception as e:
       print(f"port {port} is closed: {e}")
       return False
    
print("=" * 50)
print(f"Scanning: {host}")
print("=" * 50)
for port in ports:
    if scan_ports(host,port):
       print(f"Port {port} is open")
    else:
       print(f"Port {port} is closed")