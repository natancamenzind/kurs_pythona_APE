from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def main():
	if request.method == 'GET':
		# jeśli GET to po prostu wyświetlamy formularz
		return render_template('student.html')
	elif request.method == 'POST':	
		# jak metoda jest POST to dostajemy dane z formularza w requescie pod nazwą 'form'
		result = request.form
		# zobacz jak wyglądają przekazane dane i spróbuj je jakoś sensowniej przekazać
		return render_template("result.html", result = result)
	
if __name__ == '__main__':
	app.run()
