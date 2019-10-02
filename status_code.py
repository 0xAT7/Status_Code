import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import colorama
from colorama import Fore, Style
import eventlet
eventlet.monkey_patch()

print(Style.BRIGHT + Fore.RED + '''

	    ___  ______  _____
	   /   |/_  __/ /__  /
	  / /| | / /      / / 
	 / ___ |/ /      / /  
	/_/  |_/_/_____ /_/   
	         /_____/
''')
print(Fore.YELLOW + '''              CODED BY : A.Tarek
''')


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def process():
	try:
		filepath = sys.argv[1]
		with open (filepath,'r') as file:
			for line in file:
				with eventlet.Timeout(2):
					try:
						r = requests.get(line.strip(),verify=False)
						print (Fore.GREEN + "Domain: {} => Status Code: {}".format(line.strip(),r.status_code))
						finall=open('result.txt','a')
						finall.write('{}'.format(line))
					except:
						print(Fore.RED+"Domain: {} => Status Code: 408".format(line.strip()))
	except:
		print ("Please enter exist subdomains file\n"+Fore.GREEN+"Usage: python status_code subdomains.txt")
		sys.exit(1)
process()
print(Fore.YELLOW + "Saved in result.txt....")

