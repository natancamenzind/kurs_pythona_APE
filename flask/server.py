# SIMPLE SERVER

# importujemy Flask
from flask import Flask

# niezbędne do działania aplikacji
app = Flask(__name__)

# definijemy funkcję, która będzie odpowiedzialna za stronę
# używamy dekoratora, czyli funkcji w funkcji, podajemy URI strony
@app.route("/")
# nazwa funckji dowolna
def hello():
	# zwraca stringa, który będzie treścią strony
	return "Hello world"


# niezbędne do działania aplikacji
if __name__ == "__main__":
	app.run()

# żeby odpalić server bądź w folderze z tym plikiem i wpisz 'python server.py'