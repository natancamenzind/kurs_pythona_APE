from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'my_super_secret_key'

# połącz server1 i server2
# niech tylko zalogowany użytkownik może zapisywać, edytować i usuwać.

if __name__ == '__main__':
	app.run()