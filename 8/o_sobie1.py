my_dict = {
	'name': 'Kamil',
	'shoe number': 32
}

pytanie = input('Zadaj mi pytanie\n')
about_me = my_dict.get(pytanie)
# 1. about_me ma wartość
# 2. nie ma takiego klucza i wtedy about_me jest None

while pytanie != 'koniec':

	if about_me:
		print(about_me)
	elif 'admin123' in pytanie:
		new_key = input('Podaj nowy klucz')
		my_dict[new_key] = input('podaj nowe dane')
		print(f'{my_dict.get(new_key)} dodano do słownika')
	else: 
		print('To są dane poufne')

	pytanie = input('Zadaj mi pytanie\n')
	about_me = my_dict.get(pytanie)


for k, v in my_dict.items():
	print(f'My {k} is {v}')

