from random import randint

words = ['python', 'zespół', 'kursować', 'transcendencja']

def create_jumble(word):
	jumble = ""

	while word:
		position = randint(0, (len(word) - 1))
		jumble += word[position]
		word = word[:position] + word[(position + 1):]

	return jumble

for word in words:
	jumble = create_jumble(word)
	guess = input(f'Co to za słowo: {jumble}\n')
	while guess != word:
		guess = input('Źle! Jeszcze raz!\n')
	print('Git!')

print('Brawo! Dałeś/dałaś radę!')