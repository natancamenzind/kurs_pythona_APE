# REAL LIFE TEMPLATE

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/template')
def index():
    return render_template('name.html', name='Twój stary', )

# Teraz aplikacja ma dwie podstrony, z czego jedna to specjalna edycja świąteczna, w której możemy przekazać
# parametr 'christmas'
@app.route('/christmas')
def christmas_edition():
    return render_template('christmas.html', christmas=True, name='Twój stary')


if __name__ == "__main__":
	app.run()