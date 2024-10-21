# from models import Aluno, FichaTreino, AlunoTemFichaTreino
from app import app

@app.route('/', methods=['GET'])
def index():
    return 'Hello world'

@app.route('/listarAlunos', methods=['GET'])
def listar_alunos():
    return 'Tobias, Roberto, Carlos'