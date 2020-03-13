"""
1 = число
2 = действие
3 = число
"""

def calc(x, z, y):
	if z == "+":
		a = x + y
		print(a)
	elif z == "-":
		a = x - y
		print(a)
	elif z == "*":
		a = x * y
		print(a)
	elif z == "/":
		a = a / y
		print(a)
	elif z == "//":
		a = x // y
		print(a)
	elif z == "%":
		a = x % y
		print(a)
	else:
		print('Error')
	while True:
		calc(float(input('Enter a number')), input('Action'), float(input('Enter another number')))

calc(float(input('Enter a number')), input('Action'), float(input('Enter another number')))