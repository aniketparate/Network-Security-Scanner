#import module
import subprocess
import ipcalc
import socket
from matplotlib.pyplot import pink
from netaddr import IPAddress
import nmap

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
print(mask)
masklen = IPAddress(mask).netmask_bits()
print(masklen)

addr = ipcalc.IP(localIpAddress, mask)
network_with_cidr = str(addr.guess_network())
bare_network = network_with_cidr.split('/')[0]

scanner = nmap.PortScanner()
scanner.scan(hosts=network_with_cidr,arguments='-sn')
host_list=[x for x in scanner.all_hosts()]
print(host_list)


# print(networkIPAddresses)