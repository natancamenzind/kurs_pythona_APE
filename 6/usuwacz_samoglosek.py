# usuwacz samogłosek z 6 zajęć
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

zdanie = input('Dawaj zdanie')
result = ""
for litera in zdanie:
	if litera not in vowels:
		result += litera

		print(result)

print('Final ' + result)