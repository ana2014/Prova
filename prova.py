from flask import render_template
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def show_user_profile(name=None):
    # show the user profile for that user
    return render_template('teste.html', name=name)

@app.route('/cadastro')
def cadastro():
	return render_template('cadastro.html')

@app.route('/olar', methods=['POST'])
def olar():
	nome=request.form['nome']
	print nome
	return render_template('teste.html', name=nome)

if __name__ == '__main__':
    app.debug=True
    app.run()