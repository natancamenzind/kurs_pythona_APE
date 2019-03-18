from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def login():
	users = {
		'admin': 'admin123',
		'user11': 'asdf1234',
		'j@anek': 'Z2GL4AP74EQ2XTEQ',
	}
	if request.method == 'GET':
		# stowrz HTML który zbierze login i hasło
		return render_template("logging.html")
	elif request.method == 'POST':	
		# pobierz dane z formularza i sprawdz, czy mamy takigo użytkownika w naszej bazie
		# jeśli mamy, wyświetl komuniakt, że logowanie zakończone sukcesem, a jak nie to nie
		return render_template("logged.html", success = success)
	
if __name__ == '__main__':
	app.run()
