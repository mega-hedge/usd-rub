try: # Main code

	# Import libraries
	from requests import get # import lib for parsing
	from colorama import Fore # import lib for color font
	from time import sleep # import sleep func

	from os import system as sy # import lib for set win size
	sy('mode 19, 2') # set start win size


	while True: # Infinite while
		rub = get( 'https://www.cbr-xml-daily.ru/daily_json.js' ).json() # parsing USD
		print( f"{Fore.GREEN}1 USD = {Fore.RED}{ round( rub['Valute']['USD']['Value'] , 3) } {Fore.GREEN}RUB" ) # print USD to RUB

		sleep(5) # delay 5 sec
		sy('cls') # clear display


except: # If have errors
	sy('python -m pip install -U pip')
	sy('pip3 install colorama')
	sy('pip3 install requests')

	sy('mode 30, 3')
	input('All libraries is installed. Please, reset this program')
