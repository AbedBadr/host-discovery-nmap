#!/usr/bin/python3
import nmap
import sys

nm = nmap.PortScanner()

def run_scan(subnet):
	nm.scan(subnet, arguments="sn")

	with open('host_discovery.txt', 'w') as file:
		hosts = nm.all_hosts()
		for host in hosts:
			if nm[host].state()=='up':
				print(f'HOST: {host} \033[92m[UP]\033[0m')
				file.write(f'{host} : UP\n')

		print('Done. Hosts are saved in host_discovery.txt')

if __name__ == "__main__":
	subnet = sys.argv[1]
	run_scan(subnet)