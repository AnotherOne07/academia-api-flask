
from datetime import date
from app import db

class Aluno(db.Model):
    __tablename__ = 'aluno'

    matricula = db.Column(db.Integer, primary_key=True, nullable=False)
    numero_sessoes = db.Column(db.Integer, nullable=False)
    data_matricula = db.Column(db.Date, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    observacoes = db.Column(db.String(500))
    usuario_cpf = db.Column(db.String(11), db.ForeignKey('usuario.cpf'), nullable=False)

    # Relacionamento com a tabela 'usuario'
    usuario = db.relationship('Usuario', backref=db.backref('alunos', lazy=True))

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

class Usuario(db.Model):
    __tablename__ = 'usuario'

    cpf = db.Column(db.String(11), primary_key=True, nullable=False)
    # Outras colunas de 'usuario' (preencher conforme necessário)
