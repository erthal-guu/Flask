from flask import Flask
import os
from models.produto import db, Produto
from flask import render_template,request,redirect,url_for

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'meubanco.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/adicionar_produto', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        p = Produto(nome=nome, preco=preco)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('adicionar.html')



@app.route('/produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html',produtos= produtos)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
