# zadanie rozgrzewkowe z zajęć nr 6
# tutaj można wyjść z programu za pomocą entera
slowo = None
while slowo != '':
	slowo = input('Podaj prosze slowo')
	if slowo != '':
		i1 = int(input("podaj pierwszy indeks"))
		i2 = int(input("podaj drugi indeks"))

		wynik = slowo[i1:i2]
		print(f"Slowo {slowo} z indeksami [{i1}:{i2}] to: {wynik}")

