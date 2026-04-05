from flask import Flask, request, jsonify
import json
from models.aluno import Aluno

app = Flask(__name__)

ARQUIVO = 'alunos.json'


def ler_dados():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except:
        return []


def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)



@app.route('/alunos', methods=['POST'])
def create_aluno():
    dados = ler_dados()
    data = request.get_json()

    nova_matricula = len(dados) + 1

    novo_aluno = Aluno(
        matricula=nova_matricula,
        nome=data['nome'],
        idade=data['idade'],
        curso=data['curso']
    )

    dados.append(novo_aluno.to_dict())
    salvar_dados(dados)

    return jsonify(novo_aluno.to_dict()), 201



@app.route('/alunos', methods=['GET'])
def get_alunos():
    dados = ler_dados()
    return jsonify(dados), 200



@app.route('/alunos/<int:matricula>', methods=['GET'])
def get_aluno(matricula):
    dados = ler_dados()

    aluno = next((a for a in dados if a['matricula'] == matricula), None)

    if aluno is None:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    return jsonify(aluno), 200



@app.route('/alunos/<int:matricula>', methods=['PUT'])
def update_aluno(matricula):
    dados = ler_dados()
    data = request.get_json()

    for aluno in dados:
        if aluno['matricula'] == matricula:
            aluno['nome'] = data.get('nome', aluno['nome'])
            aluno['curso'] = data.get('curso', aluno['curso'])
            aluno['idade'] = data.get('idade', aluno['idade'])

            salvar_dados(dados)
            return jsonify(aluno), 200

    return jsonify({'erro': 'Aluno não encontrado'}), 404



@app.route('/alunos/<int:matricula>', methods=['DELETE'])
def delete_aluno(matricula):
    dados = ler_dados()

    novos_dados = [a for a in dados if a['matricula'] != matricula]

    if len(dados) == len(novos_dados):
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    salvar_dados(novos_dados)

    return jsonify({'mensagem': 'Aluno removido com sucesso'}), 200



if __name__ == '__main__':
    app.run(debug=True)