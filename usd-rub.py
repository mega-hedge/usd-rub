print('-' * 10, 'USD - RUB', '-' * 10) # print program name

try:
	from requests import get # import lib for parsing
	from time import sleep # import sleep func

	for i in range(10000):
		rub = get( 'https://www.cbr-xml-daily.ru/daily_json.js' ).json() # parsing USD
		print('1 USD =', round( rub['Valute']['USD']['Value'] , 3), 'RUB') # print USD to RUB
		sleep(3)

except:
	print('Error! Please, reset program!')

else:
	input()