from flask import Flask, render_template

app = Flask ("Restaurante")

@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/cardapio')
@app.route('/cardapio/<categoria>')
def cardapio(categoria=None):

    categorias = {
        'menuexecutivo': {
            'nome': 'Menu Executivo',
            'imagem': 'menuexecutivoinicial.png'
        },

        'nossosqueridinhos': {
            'nome': 'Os Nossos Queridinhos',
            'imagem': 'queridinhos.png'
        },
        
        'entradas': {
            'nome': 'Entradas',
            'imagem': 'entradas.png'
        },
    }

    if categoria is None:
        return render_template(
            'cardapio.html',
            categoria=None
        )

    dados_categoria = categorias.get(categoria)

    if dados_categoria is None:
        return "Categoria não encontrada", 404

    return render_template(
        'cardapio.html',
        categoria=categoria,
        nome_categoria=dados_categoria['nome'],
        imagem=dados_categoria['imagem'])


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

if __name__ == "__main__":
    app.run(debug=True)
