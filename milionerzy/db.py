milionerzy_db = {
	'prezydent': {
		'question':'Jak nazywał się drugi prezydent USA?', 
		'good': 'John Adams',
		'bad': (
		 'James Madison', 
		 'James Monroe',
		 'Andrew Jackson',
		)
	},
	'python': {
		'question':'Jak nazywa się twórca Python?', 
		'good': 'Guido van Rossum',
		'bad': (
		 'Linus Torvalds', 
		 'Ken Thompson',
		 'Grace Hopper',
		)
	},
	'Sinn Féin': {
		'question':'Sinn Féin to ...', 
		'good': 'irlandzka partia polityczna, której zbrojnym ramieniem było IRA',
		'bad': (
		 'trzecia płyta studyjna Sinéad O’Connor', 
		 "nieopublikowana za życia krótka powieść Jamesa Joyce'a",
		 'zawołanie irlandzkich lojalistów, przywiązanych do Korony Brytyjskiej',
		)
	},
	'Kubrick': {
		'question':'Stanley Kubrick nie nakręcił', 
		'good': 'Napoleona',
		'bad': (
		 'Ścieżki chwały', 
		 "Lolity",
		 "Barrego Lyndona",
		)
	},
	'Zamysłów': {
		'question':'Zamysłow to dzielnica', 
		'good': 'Rybnika',
		'bad': (
		 'Łomży', 
		 "Słupska",
		 "Legnicy",
		)
	},
	'Euscarthmus': {
		'question':'Euscarthmus to...', 
		'good': 'rodzaj ptaka z podrodziny eleni',
		'bad': (
		 'apokryficzny tekst o tańcu przypisywany Arystotelesowi', 
		 "jeden z syndromów choroby popromiennej",
		 "nazwisko jendnego z liderów greckiej partii Syriza",
		)
	},
}

import json

with open('milionerzy_db', 'w') as file:
    content = json.dumps(milionerzy_db)
    file.write(content)