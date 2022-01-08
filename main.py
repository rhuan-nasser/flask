from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'mestra'

equipamentos = list()

class Equipamentos:
    def __init__(self, marca, modelo, patrimonio):
        self.marca = marca
        self.modelo = modelo
        self.patrimonio = patrimonio

# Template de LOGIN
@app.route('/')
def login():
    return render_template('login.html')


# Verifica se a senha é válida
@app.route('/verifica', methods=['POST'])
def verifica():
    login = request.form['login']
    senha = request.form['password']

    if login == 'teste' and senha == '123456':
        session['usuario_logado'] = request.form['login']
        flash(request.form['login'] + ' Logado com Sucesso!')
        return redirect('/inicio')
    else:
        flash('Usuário ou senha incorreto. Tente novamente!')
        return redirect('/')


# Logout
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')


# Template de cadastro dos equipamentos
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


# Acrescenta as informações na lista equipamentos
@app.route('/criar', methods=['POST',])
def criar():
    marca = request. form['marca']
    modelo = request. form['modelo']
    patrimonio = request. form['patrimonio']
    equipamento = Equipamentos(marca, modelo, patrimonio)
    equipamentos.append(equipamento)
    return render_template('lista.html', equipamentos=equipamentos)



@app.route('/inicio')
def inicio():
    return render_template('lista.html', equipamentos=equipamentos)





app.run(debug=True)