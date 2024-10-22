CREATE TABLE IF NOT EXISTS academia (
  codigo_unidade INTEGER NOT NULL,
  telefone JSONB NOT NULL,
  rua VARCHAR(50) NOT NULL,
  cep VARCHAR(8) NOT NULL,
  numero VARCHAR(4) NOT NULL,
  nome VARCHAR(100) NOT NULL,
  horario_abertura TIME NOT NULL,
  horario_fechamento TIME NOT NULL,
  PRIMARY KEY (codigo_unidade)
);

CREATE TABLE IF NOT EXISTS usuario (
  cpf VARCHAR(11) NOT NULL,
  cep VARCHAR(8),
  numero_casa VARCHAR(4),
  rua VARCHAR(100),
  usuario VARCHAR(50) NOT NULL,
  palavra_forte VARCHAR(50) NOT NULL,
  primeiro_nome VARCHAR(100) NOT NULL,
  sobrenome VARCHAR(100) NOT NULL,
  data_nascimento DATE NOT NULL,
  telefone JSONB NOT NULL,
  academia_codigo_unidade INTEGER NOT NULL,
  PRIMARY KEY (cpf),
  UNIQUE (usuario),
  FOREIGN KEY (academia_codigo_unidade)
    REFERENCES academia (codigo_unidade)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS aluno (
  matricula INTEGER NOT NULL,
  numero_sessoes INTEGER NOT NULL,
  data_matricula DATE NOT NULL,
  altura FLOAT NOT NULL,
  peso FLOAT NOT NULL,
  observacoes VARCHAR(500),
  usuario_cpf VARCHAR(11) NOT NULL,
  PRIMARY KEY (matricula),
  	FOREIGN KEY (usuario_cpf)
    REFERENCES mydb.usuario (cpf)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS ficha_treino (
  tipo SMALLINT NOT NULL,
  objetivo VARCHAR(100) NOT NULL DEFAULT 'Ganhar Massa',
  id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS aluno_acompanha_ficha_treino (
  id INTEGER NOT NULL,
	data DATE NOT NULL,
  aluno_matricula INTEGER NOT NULL,
  ficha_treino_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (aluno_matricula)
    REFERENCES aluno (matricula)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (ficha_treino_id)
    REFERENCES ficha_treino (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);