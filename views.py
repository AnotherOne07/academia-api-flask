from flask import Blueprint, jsonify, request
from models import Academia, Usuario, Aluno, FichaTreino, AlunoAcompanhaFichaTreino
from app import db

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/', methods=['GET'])
def index():
    return 'Hello world'

#------------------------------------------------------------------------------
# ROTAS PARA ALUNO
# LISTAR TODOS - OK
@app_routes.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()

    lista_alunos = []
    
    for aluno in alunos:
        aluno_dict = aluno.to_dict()
        usuario = Usuario.query.filter_by(cpf=aluno.usuario_cpf).first()

        if usuario:
            aluno_dict['usuario'] = usuario.to_dict()
        
        lista_alunos.append(aluno_dict)

    return jsonify(lista_alunos), 200

# LISTAR ALUNO - OK
@app_routes.route('/alunos/<int:matricula>', methods=['GET'])
def get_aluno(matricula):
    aluno = Aluno.query.get(matricula)
    if aluno is None:
        return jsonify({'message': 'Aluno não encontrado!'}), 404
    
    usuario = Usuario.query.filter_by(cpf=aluno.usuario_cpf).first()

    aluno = aluno.to_dict()
    
    # Verifica se usuario existe
    if usuario:
        aluno['usuario'] = usuario.to_dict()
    
    return jsonify(aluno), 200

# CRIAR ALUNO - OK
@app_routes.route('/criarAluno', methods=['POST'])
def criar_aluno():
    data = request.get_json()

    # Verifica se as chaves necessárias estão presentes
    if 'usuario' not in data or 'aluno' not in data:
        return jsonify({'error': 'Requisição inválida. Dados de "usuario" e "aluno" são obrigatórios.'}), 400

    usuario_data = data['usuario']
    aluno_data = data['aluno']

    # Verifica se todos os dados do usuário estão presentes
    if not all(k in usuario_data for k in ('cpf', 'usuario', 'palavra_forte', 'primeiro_nome', 'sobrenome', 'data_nascimento', 'telefone', 'academia_codigo_unidade')):
        return jsonify({'error': 'Dados insuficientes para o usuário.'}), 400

    # Verifica se todos os dados do aluno estão presentes
    if not all(k in aluno_data for k in ('matricula', 'numero_sessoes', 'data_matricula', 'altura', 'peso')):
        return jsonify({'error': 'Dados insuficientes para o aluno.'}), 400

    # Criação do model de usuário
    novo_usuario = Usuario(
        cpf=usuario_data['cpf'],
        cep=usuario_data.get('cep'),
        numero_casa=usuario_data.get('numero_casa'),
        rua=usuario_data['rua'],
        usuario=usuario_data['usuario'],
        palavra_forte=usuario_data['palavra_forte'],
        primeiro_nome=usuario_data['primeiro_nome'],
        sobrenome=usuario_data['sobrenome'],
        data_nascimento=usuario_data['data_nascimento'],
        telefone=usuario_data['telefone'],
        academia_codigo_unidade=usuario_data['academia_codigo_unidade']
    )

    # Criação do model de aluno
    novo_aluno = Aluno(
        matricula=aluno_data['matricula'],
        numero_sessoes=aluno_data['numero_sessoes'],
        data_matricula=aluno_data['data_matricula'],
        altura=aluno_data['altura'],
        peso=aluno_data['peso'],
        observacoes=aluno_data.get('observacoes'),
        usuario_cpf=usuario_data['cpf']
    )

    # Adicionar os objetos à sessão e fazer o commit no banco de dados
    try:
        db.session.add(novo_usuario)
        db.session.add(novo_aluno)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Reverter a transação em caso de erro
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Aluno criado com sucesso!'}), 201

# ATUALIZAR ALUNO - OK
@app_routes.route('/atualizarAluno', methods=['POST'])
def atualizar_aluno():
    data = request.get_json()

    # Extrair os dados do JSON
    aluno_data = data.get('aluno')
    usuario_data = data.get('usuario')

    try:
        # Buscar o aluno pela matrícula
        aluno = Aluno.query.filter_by(matricula=aluno_data['matricula']).first()

        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        # Buscar o usuário pelo CPF associado ao aluno
        usuario = Usuario.query.filter_by(cpf=aluno.usuario_cpf).first()

        if not usuario:
            return jsonify({"erro": "Usuário associado não encontrado"}), 404

        # Atualizar dados do aluno
        if aluno_data:
            aluno.numero_sessoes = aluno_data.get('numero_sessoes', aluno.numero_sessoes)
            aluno.data_matricula = aluno_data.get('data_matricula', aluno.data_matricula)
            aluno.altura = aluno_data.get('altura', aluno.altura)
            aluno.peso = aluno_data.get('peso', aluno.peso)
            aluno.observacoes = aluno_data.get('observacoes', aluno.observacoes)

        # Atualizar dados do usuário
        if usuario_data:
            usuario.cep = usuario_data.get('cep', usuario.cep)
            usuario.numero_casa = usuario_data.get('numero_casa', usuario.numero_casa)
            usuario.rua = usuario_data.get('rua', usuario.rua)
            usuario.palavra_forte = usuario_data.get('palavra_forte', usuario.palavra_forte)
            usuario.primeiro_nome = usuario_data.get('primeiro_nome', usuario.primeiro_nome)
            usuario.sobrenome = usuario_data.get('sobrenome', usuario.sobrenome)
            usuario.data_nascimento = usuario_data.get('data_nascimento', usuario.data_nascimento)
            usuario.telefone = usuario_data.get('telefone', usuario.telefone)
            usuario.academia_codigo_unidade = usuario_data.get('academia_codigo_unidade', usuario.academia_codigo_unidade)

        # Transação utilizada para garantir consistência nas alterações
        db.session.commit()

        return jsonify({
            "mensagem": "Aluno atualizado com sucesso",
            "aluno": aluno.to_dict(),
            "usuario": usuario.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500

# DELETAR ALUNO - OK
@app_routes.route('/deletarAluno/<int:matricula>', methods=['GET'])
def deletar_aluno(matricula):
    try:
        # Buscar o aluno pela matrícula
        aluno = Aluno.query.filter_by(matricula=matricula).first()

        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        # Buscar o usuário associado ao aluno (se for necessário deletar também)
        usuario = Usuario.query.filter_by(cpf=aluno.usuario_cpf).first()

        # Excluir o aluno
        db.session.delete(aluno)
        
        # Excluir o usuário associado ao aluno
        if usuario:
            db.session.delete(usuario) 

        # Commit na transação
        db.session.commit()
        return jsonify({"mensagem": "Aluno excluído com sucesso"}), 200

    except Exception as e:
        db.session.rollback()  # Em caso de erro, desfazer a transação
        return jsonify({"erro": str(e)}), 500

#-----------------------------------------------------------------------------
# ROTAS PARA FICHA DE TREINO
@app_routes.route('/listarFichasTreino', methods=['GET'])
def listar_fichas_treino():
    fichas = FichaTreino.query.all()

    lista_fichas = [ficha.to_dict() for ficha in fichas]

    return jsonify(lista_fichas), 200