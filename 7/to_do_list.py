to_do_list = []
possible_opperations = ['add', 'remove', 'show_all', 'insert', 'pop', 'clear']

print('Hello to your to do list app!\nYou can {}'.format(possible_opperations))
action = ' '
while action:
	action = input('What would you like to do?')
	if action == 'add':
		to_do_thing = input('what would you like to add?')
		to_do_list.append(to_do_thing)
	elif action == 'remove':
		thing_to_remove = input('What to remove?')
		to_do_list.remove(thing_to_remove)
	elif action == 'show_all':
		print(to_do_list)
	elif action == 'insert':
		to_do_thing = input('what would you like to add?')
		index = int(input('where?'))
		to_do_list.insert(index, to_do_thing)
	elif action == 'pop':
		index = int(input('where?'))
		to_do_list.pop(index)
	elif action == 'clear':
		to_do_list.clear()
