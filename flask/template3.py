# TEMPLATKI I PĘTLE

from flask import Flask, render_template

app = Flask(__name__)

users = [{'login': 'admin', 'password': 'admin123'}, {'login': 'user', 'password': 'kocham_mame'}]

@app.route('/loop')
def loop_test():
    return render_template('loop.html', name='Twój stary', users=users)


if __name__ == "__main__":
	app.run()