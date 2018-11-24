def sum(a,b):
	return a + b

def minus(a, b):
	return a - b

def divide(a, b):
	return a / b	

value = 0
def start():
	num1 = int(input('Number one'))
	num2 = int(input('Number two'))
	to_do1 = input('What to do?')
	if to_do1 == 'sum':
		value = sum(num1, num2)
	elif to_do1 == 'minus':
		value = minus(num1, num2)
	elif to_do1 == 'divide':
		value = divide(num1, num2)
	print('Our value is {}'.format(value))

