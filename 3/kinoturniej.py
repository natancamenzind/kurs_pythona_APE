# Pierwsze zadanie z trzecich zajęć, w prezentacji jako 'teleturniej'
print('Czy jesteś gotowy na przygodę życia?')
name = input('Jak się nazywasz anonimowa internatuko?')
print('Witaj {} w naszej grze! Zadam Ci trzy pytania, które zadecydują o Twoim przyszłym losie.'.format(name))

score = 0
likes_tarantino = False
def good_answer():
	print('Świetnie!')
	score += 1


# pytanie 1
odp1 = input('Jakim filmem debiutował Quentin Tarantino?')
if odp1 == 'Wściekłe psy' or odp1 == 'Reservoir dogs':
	likes_tarantino = True
	good_answer()
else:
	print('Niestety błąd! Były to Wściekłe psy')

# pytanie 2
odp2 = input('W którym roku zmarł Andrzej Wajda?')
if odp2 == '2017':
	good_answer()
else:
	print('Cóż {} to niewłaściwa odpowiedź'.format(name))

# pytanie 3
odp3 = input('Jaki Polski film jako jedyny zdobył Oskara za najlepszy film zagraniczny i kto go wyreżyserował?')
if ('Ida' in odp3) and ('Pawlikowski' in odp3):
	good_answer()
else:
	print('To "Ida" Pawła Pawlikowskiego!')

print('Twój wynik to {}/3 puntky'.format(score))
if score == 3:
	print('Twoja wiedza o filmie przyniesie Ci szczęście w miłości!')
elif score > 0:
	print('Nie jest źle!')
else:
	print('Kino to nie Twoje paliwo, co?')

if likes_tarantino:
	print('I fajnie, że lubisz Tarantino!')



	
