from flask import Flask, render_template

app = Flask ("Restaurante")

@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/home')
def livros():
    return render_template('home.html')

@app.route('/cardapio')
def perfil():
    return render_template('cardapio.html')

@app.route('/contato')
def home():
    return render_template('contato.html')

@app.route('/sobre')
def home():
    return render_template('sobre.html')

app.run(debug=True)
