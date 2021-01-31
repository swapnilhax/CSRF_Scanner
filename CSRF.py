from socket import gethostname,gethostbyname
from urllib import request
import time,os
import sys
from urllib.request import urlopen
from colorama import Fore,Style
import urllib
import requests

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'

if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(RED + """  

  #####   #####  ######  #######     #####                                            
 #     # #     # #     # #          #     #  ####    ##   #    # #    # ###### #####  
 #       #       #     # #          #       #    #  #  #  ##   # ##   # #      #    # 
 #        #####  ######  #####       #####  #      #    # # #  # # #  # #####  #    # 
 #             # #   #   #                # #      ###### #  # # #  # # #      #####  
 #     # #     # #    #  #          #     # #    # #    # #   ## #   ## #      #   #  
  #####   #####  #     # #           #####   ####  #    # #    # #    # ###### #    # 
                                                                                      
                                                                                          
    """  + END+BLUE+'CSRF Scanner'.format(RED, END).center(69) +
    '\n' + '\tMade ^_^ by: {}Sw4pn1l'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
    '\n' + '\tVersion: {}1.0{}\n'.format(YELLOW, END).center(80) + '\n')
else:
#    sys.exit('Usage: python headers_check.py')
    os.system("clear || cls")


#	print("Example: http://google.com/login.php")
#	url = input("Enter Website :- ")
#	headers = str(urlopen(url).headers.headers).lower() #Fetches headers of webpage
#	data = br.open(url).read()
#	print(data)
#	if 'type="hidden"' not in data:
#		print("CSRF Vulnerability")
#	else:
#		print("CSRF Enabled")


#os.system("clear")
print(Fore.GREEN + "[1] CSRF Vulnerability")
print(Style.RESET_ALL)

x = input("Choose first option >\n") 


if x == "1":


	url = input("Enter Website :- \n\n")
	r = requests.get(url).text

	if 'type="hidden"' in r or 'name="CSRFToken"' in r or 'name="authenticity_token"' in r:
		print("\nNot Vulnerable to CSRF")
	else:
		print(Fore.RED + "\nCSRF Vulnerable")
		print(Style.RESET_ALL)

else:
    print("\x1b[31m Please Try Again . . .")

