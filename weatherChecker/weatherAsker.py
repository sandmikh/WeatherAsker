# -*- coding: utf-8 -*-
import pyowm

def askWeatherIn(cityName):
	# Инициализация запроса погоды с API-ключом и установкой русского языка.
	owm = pyowm.OWM('05fc4fbdd621b7c0eba4b19b14a41ef0', language='ru')
	# Получаем общую погоду и значение температуры в указанном городе.
	try:
		weather = owm.weather_at_place(cityName).get_weather()
		# Используется шкала Цельсий. Значение "temp" указывает на среднее значение.
		return weather.get_temperature("celsius")["temp"]
	except:
		print("Сожалеем, но получить температуру для города " + str(cityName) + " невозможно, введите другое имя!")
		exit()

def showWeather(temperature, cityName):
	print("в городе " + str(cityName) + " сейчас: " + str(temperature) + " градусов по Цельсию.")