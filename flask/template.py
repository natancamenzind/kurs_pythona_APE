# TEMPLATE PRESENTATION
from flask import Flask

app = Flask(__name__)

# strona będzie dostępna pod uri /template
@app.route('/template')
def index():
	# chcemy wykorzystać zmienną, żeby strona nie była zawsze taka sama
    user = {'username': 'Anna'}
    # zwracamy stringa, który jest HTMLem
    return '''
		<html>
		    <head>
		        <title>Home Page</title>
		    </head>
		    <body>
		        <h1>Hello, {}!</h1>
		    </body>
		</html>'''.format(user.get('username'))


if __name__ == "__main__":
	app.run()