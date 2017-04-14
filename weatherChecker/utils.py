# -*- coding: utf-8 -*-
# Модуль вспомогательных утилит.

# Функция запроса названия города.
def askCityName():
	cityName = str(input("Введите название города: "))
	if not cityName:
		print("Извините, название города не может быть пустым!")
		exit()
	else:
		return cityName