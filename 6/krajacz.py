word = None
while word != "":
	word = input('Wprowadź słowo\n')
	if not word:
		break
	start = int(input('Indeks początkowy\n'))
	end = int(input('Indeks końcowy\n'))
	print('Słowo {} z indeksami [{}:{}] '.format(word, start, end) + word[start:end])
	print('Aby zakończyć wciśniej Enter')
