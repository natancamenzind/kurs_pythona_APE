from random import randint

word123 = 'python'
word_list = ['dupa', 'pociąg', 'helikopter', 'hakatomba']

def mieszacz(word):
	new_word = ""
	while word:
		posision = randint(0, len(word) - 1)
		new_word += word[posision]
		word = word[:posision] + word[posision + 1:]

	return new_word
for word123 in word_list:
	zmieszane_slowo = mieszacz(word123)

	quese = input('Zgadnij co to za słow {}'.format(zmieszane_slowo))
	while quese != word123:
		quese = input('ŹLE!!! Jeszcze raz')
	print('Pięknie!')
print('Brawo! Dobiłeś_aś do końca tej wielkiej przygody!')