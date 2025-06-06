from flask import Flask, render_template, request
import csv
from twilio.rest import Client

app = Flask(__name__)

# CREDENCIAIS DA TWILIO (com espaços removidos!)
account_sid = 'ACb851bdc7d8ea96e3f8e156c3a21801d2'
auth_token = 'c3df904f62de76e8b12c772940da0a8b'
twilio_number = 'whatsapp:+14155238886'
meu_numero = 'whatsapp:+557991763141'

client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    telefone = request.form['telefone']

    with open('dados.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone])

    mensagem = f"✅ Novo cadastro na Caselândia!\n👤 {nome}\n📱 {telefone}"
    client.messages.create(
        from_=twilio_number,
        to=meu_numero,
        body=mensagem
    )

    return "Cadastro realizado com sucesso! ✅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

