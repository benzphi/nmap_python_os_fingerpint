import nmap #works only with nmap installed on machine
import sys
from pprint import pprint

def scanitself():
    nm = nmap.PortScanner()
    print('\nStarted, this operation might take some time depending on how many ports you decided to scan\n')
    nmscan = nm.scan(sys.argv[1], sys.argv[2], arguments='-O')

    pprint(nmscan)

    with open(sys.argv[3], "w") as f:
        f.write(str(nmscan))

    print('finished')

while True:
    print('start nmap scan on '+str(sys.argv[1])+' and save it to '+str(sys.argv[3])+' y/n')
    one = input()
    if one == "y":
        scanitself()
        break
    elif one == "n":
        exit()
    else:
        pass






print("\n...")