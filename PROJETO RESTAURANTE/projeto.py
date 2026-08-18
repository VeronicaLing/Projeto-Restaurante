from flask import Flask, render_template

app = Flask ("Restaurante")

@app.route('/')
def HomePage():
    return render_template('base.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/cardapio/menuexecutivo')
def menuexecutivo():
    return render_template('menuexecutivo.html')

@app.route('/cardapio/bebidas')
def bebidas():
    return render_template('bebidas.html')

@app.route('/cardapio/aves')
def aves():
    return render_template('aves.html')

@app.route('/cardapio/carnes')
def carnes():
    return render_template('carnes.html')

@app.route('/cardapio/teppanyaki')
def teppanyaki():
    return render_template('teppanyaki.html')

@app.route('/cardapio/frutosdomar')
def frutosdomar():
    return render_template('frutosdomar.html')

@app.route('/cardapio/arroz')
def arroz():
    return render_template('arroz.html')

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

app.run(debug=True)
