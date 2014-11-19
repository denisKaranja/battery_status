def factorial(number):
	if number == 1 or number == 0:
		return 1
	else:
		result = number * factorial(number -1)
		return result

print factorial(10)