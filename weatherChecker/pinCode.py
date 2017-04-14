# -*- coding: utf-8 -*-
# запрашиваем pin код с клавиатуры.
def askPinCode():
	return str(input("Введите пин код: "))

# Всесторонне проверяем корректность введённого пользователем пинкода.
def makeSurePinCodeIsValid(code):
	makeSureCodeIsNotEmpty(code)
	makeSureCodeIsDigitBased(code)
	makeSureCodeIsCorrect(code)

# Служебные функции
def makeSureCodeIsNotEmpty(code):
	if not code:
		print("Код не может состоять из пустой строки!")
		exit()

def makeSureCodeIsDigitBased(code):
	notOnlyDigits = not code.isdigit()
	if notOnlyDigits:
		print("Код должен состоять только из цифр!")
		exit()

def makeSureCodeIsCorrect(code):
	if code == "20090909":
		print("Вы можете узнать прогноз погоды.")
	else:
		print("Вы не можете возпользоваться этой программой.")
		exit()