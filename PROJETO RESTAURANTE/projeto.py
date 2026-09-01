from flask import Flask, render_template

app = Flask ("Restaurante")

@app.route('/')
def HomePage():
    return render_template('index.html')

@app.route('/cardapio/<categoria>')
def categoria(categoria):

    categorias = {
        'menuexecutivo': 'Menu Executivo',
        'bebidas': 'Bebidas',
        'aves': 'Aves',
        'carnes': 'Carnes',
        'teppanyaki': 'Teppanyaki',
        'frutosdomar': 'Frutos do Mar',
        'arroz': 'Arroz',
        'queridinhos': 'Queridinhos',
    }

    nome_categoria = categorias.get(categoria)

    if not nome_categoria:
        return "Categoria não encontrada", 404

    return render_template(
        'categoria.html',
        categoria=nome_categoria
    )

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
