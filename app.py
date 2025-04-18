from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista simples pra guardar depoimentos (seria um banco de dados futuramente)
depoimentos = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/depoimentos', methods=['GET', 'POST'])
def pagina_depoimentos():
    if request.method == 'POST':
        nome = request.form['nome']
        mensagem = request.form['mensagem']
        if nome and mensagem:
            depoimentos.append({'nome': nome, 'mensagem': mensagem})  # Adiciona depoimento
        return redirect('/depoimentos')  # Recarrega página pra ver o novo depoimento
    return render_template('depoimentos.html', depoimentos=depoimentos)

if __name__ == '__main__':
    app.run(debug=True)
