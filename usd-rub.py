# Import libraries
from requests import get # import lib for parsing
from colorama import Fore # import lib for color font
from time import sleep # import sleep func

from os import system as sy # import lib for set win size
sy('mode 24,2') # set start win size


usd = int( input( f'{Fore.GREEN}Enter usd: {Fore.RED}') )
sy('cls') # clear display

while True: # Infinite while
	rub = get( 'https://www.cbr-xml-daily.ru/daily_json.js' ).json() # parsing USD
	print( f"{Fore.RED}{usd} {Fore.GREEN}USD = {Fore.RED}{ round( rub['Valute']['USD']['Value']  * usd , 3) } {Fore.GREEN}RUB" ) # print USD to RUB

	sleep(5) # delay 5 sec
	sy('cls') # clear display
