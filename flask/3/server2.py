from flask import Flask, render_template, session
app = Flask(__name__)
# poniższe musi się pojawić, bez tego Flask nie pozwoli Ci zapisywać nic w sesji (o tym będzie dalej)
app.secret_key = 'my_super_secret_key'

"""
Na początku przygody z Flaskiem przygotowaliśmy logowanie. Jednak to dopiero początek. Z zasady protokoły
HTTP i HTTPS są bezsatnowe, czyli przy każdym wejściu na stronę zaczynają niejako "od początku". Żeby móc
zachować stan (spowodować, że użytkowniczka będzie cały czas zalogowana, że jej ustawienia kolorystyczne
strony będą zapamiętane itp.) korzystamy z sesji i ciasteczek. Teraz wykorzystamy sesję, żeby nasze 
logowanie  było trwałe.
"""
# Wykorzystaj swój kod z pierwszego spotkania poświęconego Flaskowi
@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.method == 'GET':
		# formuarz do logowania
		return render_template("login.html")
	elif request.method == 'POST':	
		success = False
		# pobierz dane z formularza i sprawdz, czy mamy takigo użytkownika w naszej bazie z pliku
		if success:
			# session importujemy z paczki samego Flaska, działa prawie identycznie jak słownik
			session['logged_in'] = True
		return render_template("login.html")

@app.route('/')
def index():
	# dane z sesji wyciągamy jak ze słownika
	if not session.get('logged_in') == True:
		return login()
	return 'GOOD HAKER'

if __name__ == '__main__':
	app.run()