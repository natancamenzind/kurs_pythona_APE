from random import randint


random_number = randint(1, 10)
user_numer = input("Podaj liczbe od 1 do 10")
tries = 1
while int(user_numer) != random_number:

	tries += 1
	user_numer = input('Sporóbuj jeszcze raz!')


print(f'KONIEC po {tries} próbach')

