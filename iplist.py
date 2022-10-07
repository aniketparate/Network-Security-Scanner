#import module
import subprocess
import ipcalc
import socket
from netaddr import IPAddress

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

localIpAddress = get_ip()
proc = subprocess.Popen('ipconfig',stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if localIpAddress.encode() in line:
        break
mask = proc.stdout.readline().rstrip().split(b':')[-1].replace(b' ',b'').decode()
masklen = IPAddress(mask).netmask_bits()

addr = ipcalc.IP(localIpAddress, mask)
network_with_cidr = str(addr.guess_network())
bare_network = network_with_cidr.split('/')[0]

IPs = subprocess.run(['nmap','-sn', network_with_cidr],capture_output=True,text=True)

print(IPs)