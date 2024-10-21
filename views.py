from flask import Blueprint, jsonify
from models import Aluno, FichaTreino, AlunoAcompanhaFichaTreino

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/', methods=['GET'])
def index():
    return 'Hello world'

# @app.route('/listarAlunos', methods=['GET'])
# def listar_alunos():
#     return 'Tobias, Roberto, Carlos'

# @app.route('/criarAluno', methods=['POST'])
# def criar_aluno():
#     return 'Aluno criado com sucesso'

# # ROTAS PARA FICHA DE TREINO

@app_routes.route('/listarFichasTreino', methods=['GET'])
def listar_fichas_treino():
    fichas = FichaTreino.query.all()

    lista_fichas = [ficha.to_dict() for ficha in fichas]

    return jsonify(lista_fichas), 200