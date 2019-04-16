from flask import Flask, render_template
app = Flask(__name__)
"""
Dzisiaj poznamy widoki związe z CRUD, czyli podstawowymi funkcjami treści.
Jeśli mamy bazę danych dotyczącą np. filmów, chcemy mieć możliwość robienia z naszymi filmami kilku 
podstawowych rzeczy. Chcemy dodawać nowe, przeglądać już dodane (wszystkie na raz jak i pojedynczo),
edytować oraz usuwać. W skrócie CRUD, czyli Create, Read, Update, Delete.
"""
 
@app.route("/")
def index():
	# Stwórz stronę 
	return "Index!"
 
@app.route("/add")
def movie_create():
	# wyświetl formularz, który pozwala dodać film. Zapytaj o tytuł, reżyserię, rok produkcji i gatunek.
	# Zapisz informacje o filmie w pliku.
	# Użyj metod GET i POST
	return render_template('movie_form.html')
 
@app.route("/movies/<string:title>/")
def movie_detail(title):
	# dzięki tak sformatowanemu adresowi funkcja 'movie_detail() przyjmie z adresu tutył filmu'
	# czyli jeśli wejdziesz na stronę 127.0.0.1:5000/movies/interstellar pod zmienną lokalną title będziemy
	# mieli string 'interstellar'. Korzystając z tej zmiennej wyciągnij dany film z bazy i pokaż wszystkie informacje
	return render_template('movie_detail.html')

@app.route("/movies-list/")
def movie_detail():
	# wyciągnij wszystkie filmy z bazy, pokaż tylko tytuły i rok produkcji w liscie.
	# jeśli wiesz jak umieść pod tutułem każdego filmu link do widoku szczegółowego, zrób to
	return render_template('movies_list.html')

@app.route("/movies/<string:title>/edit/")
def movie_edit(title):
	# widok podobny do 'movie_create', z tą różnicą, że teraz napisujemy istniejący film
	# uzupełnij wstępnie dane formularza już zapisanymi danymi
	# w GETcie wyświetl formularz, w POSTcie zapisz zmiany
	return render_template('movie_edit.html')


@app.route("/movies/<string:title>/delete/")
def movie_delete(title):
	# jak wyżej, tylko że usuwamy. 
	# W metodzie GET wyswietl komunikat typu "Czy na pewno chcesz usunać film X", w metodzie POST faktycznie
	# usuń film i wyświetl komunikat typu "Usunięto film X"
	return render_template('movie_delete.html')

 
if __name__ == "__main__":
	app.run()