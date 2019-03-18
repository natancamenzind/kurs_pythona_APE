from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/register', methods = ['POST', 'GET'])
def register():
	if request.method == 'GET':
		# stowrz HTML który zbierze login i hasło dwa razy (jak to zwykle w necie bywa)
		return render_template("create.html")
	elif request.method == 'POST':
		# sprawdź czy oba hasła się zgadzają, jeśli nie, wyświetl komuniakt
		# otwórz bazę z pliku, sprawdź czy mamy już takiego użytkownika
		# jeśli mamy, wyświetl o tym komunikat
		# jeśli nie mamy, zapisz dane tego, zamknij bazę 
		return render_template("created_or_not.html", success=success, errors=errors)

@app.route('/login', methods = ['POST', 'GET'])
def logging():
	# oczywiście skorzystaj z tego co zrobiłeś/aś w poprzednim pliku
	if request.method == 'GET':
		# formuarz do logowania
		return render_template("logging2.html")
	elif request.method == 'POST':	
		# pobierz dane z formularza i sprawdz, czy mamy takigo użytkownika w naszej bazie z pliku
		return render_template("logged2.html", success=success)
	
if __name__ == '__main__':
	app.run()