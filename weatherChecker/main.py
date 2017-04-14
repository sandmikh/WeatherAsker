# -*- coding: utf-8 -*-
# Главный модуль программы, точка входа.

from weatherChecker.pinCode 		import askPinCode, makeSurePinCodeIsValid
from weatherChecker.utils 			import askCityName
from weatherChecker.weatherAsker 	import askWeatherIn, showWeather

def start():
	code = askPinCode()
	makeSurePinCodeIsValid(code)
	cityName = askCityName()
	print("проверяем введённый город: " + cityName)
	temperature = askWeatherIn(cityName)
	showWeather(temperature, cityName)

if __name__ == "main":	
	start()
