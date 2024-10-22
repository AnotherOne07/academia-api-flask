
from datetime import date
from app import db

class Academia(db.Model):
    __tablename__ = 'academia'

    codigo_unidade = db.Column(db.Integer, primary_key=True, nullable=False)
    telefone = db.Column(db.JSON, nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    numero = db.Column(db.String(4), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    horario_abertura = db.Column(db.Time, nullable=False)
    horario_fechamento = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f"<Academia(codigo_unidade={self.codigo_unidade}, nome='{self.nome}', horario_abertura='{self.horario_abertura}', horario_fechamento='{self.horario_fechamento}')>"

    def to_dict(self):
        return {
            'codigo_unidade': self.codigo_unidade,
            'telefone': self.telefone,
            'rua': self.rua,
            'cep': self.cep,
            'numero': self.numero,
            'nome': self.nome,
            'horario_abertura': self.horario_abertura.isoformat() if self.horario_abertura else None,
            'horario_fechamento': self.horario_fechamento.isoformat() if self.horario_fechamento else None
        }
    
class Usuario(db.Model):
    __tablename__ = 'usuario'

    cpf = db.Column(db.String(11), primary_key=True, nullable=False)
    cep = db.Column(db.String(8), nullable=True)
    numero_casa = db.Column(db.String(4), nullable=True)
    rua = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), nullable=False, unique=True)
    palavra_forte = db.Column(db.String(50), nullable=False)
    primeiro_nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.JSON, nullable=False)
    academia_codigo_unidade = db.Column(db.Integer, db.ForeignKey('academia.codigo_unidade'), nullable=False)

    def __repr__(self):
        return f"<Usuario(cpf='{self.cpf}', usuario='{self.usuario}', primeiro_nome='{self.primeiro_nome}', sobrenome='{self.sobrenome}')>"

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'cep': self.cep,
            'numero_casa': self.numero_casa,
            'rua': self.rua,
            'usuario': self.usuario,
            'palavra_forte': self.palavra_forte,
            'primeiro_nome': self.primeiro_nome,
            'sobrenome': self.sobrenome,
            'data_nascimento': self.data_nascimento.isoformat() if self.data_nascimento else None,
            'telefone': self.telefone,
            'academia_codigo_unidade': self.academia_codigo_unidade
        }

class Aluno(db.Model):
    __tablename__ = 'aluno'

    matricula = db.Column(db.Integer, primary_key=True, nullable=False)
    numero_sessoes = db.Column(db.Integer, nullable=False)
    data_matricula = db.Column(db.Date, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    observacoes = db.Column(db.String(500), nullable=True)
    usuario_cpf = db.Column(db.String(11), db.ForeignKey('usuario.cpf'), nullable=False)

    def __repr__(self):
        return f"<Aluno(matricula={self.matricula}, usuario_cpf='{self.usuario_cpf}', data_matricula='{self.data_matricula}')>"

    def to_dict(self):
        return {
            'matricula': self.matricula,
            'numero_sessoes': self.numero_sessoes,
            'data_matricula': self.data_matricula.isoformat() if self.data_matricula else None,
            'altura': self.altura,
            'peso': self.peso,
            'observacoes': self.observacoes,
            'usuario_cpf': self.usuario_cpf
        }

class FichaTreino(db.Model):
    __tablename__ = 'ficha_treino'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.SmallInteger, nullable=False)
    objetivo = db.Column(db.String(100), nullable=False, default='Ganhar Massa')

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'objetivo': self.objetivo
        }

class AlunoAcompanhaFichaTreino(db.Model):
    __tablename__ = 'aluno_acompanha_ficha_treino'

    data = db.Column(db.Date, nullable=False)
    aluno_matricula = db.Column(db.Integer, db.ForeignKey('aluno.matricula'), primary_key=True, nullable=False)
    ficha_treino_id = db.Column(db.Integer, db.ForeignKey('ficha_treino.id'), primary_key=True, nullable=False)

    # Relacionamentos
    aluno = db.relationship('Aluno', backref=db.backref('fichas_treino', lazy=True))
    ficha_treino = db.relationship('FichaTreino', backref=db.backref('alunos', lazy=True))

    def to_dict(self):
        return {
            'data': self.data.isoformat(),
            'aluno_matricula': self.aluno_matricula,
            'ficha_treino_id': self.ficha_treino_id
        }