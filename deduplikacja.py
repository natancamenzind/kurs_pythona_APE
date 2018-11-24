# dodatkowe zadania z list
answer =[]
for i in range(2500, 3800):
	if i%7 == 0 and i%5 != 0:
		answer.append(i)

print(answer)



def deduplicate(my_list):
	new_list = []
	for element in my_list:
		if element not in new_list:
			new_list.append(element)	
	return new_list


asdf = [1,2,2,12,21,12,12,12,12,1,2,1]
new_asdf = deduplicate(asdf) # [1, 2 ,12, 21]
