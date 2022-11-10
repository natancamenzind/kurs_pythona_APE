more = True
num  = 2
while more:
	num = num * 2
	print(f'Power of two: {num}')
	want_more = input('Whant to see more powers of 2?\n'
					  'y for yes, n for no\n')
	if want_more == 'y':
		more = True
	elif want_more == 'n':
		more = False
	else:
		input("I don't understand you!")

print('Ok thanks!')