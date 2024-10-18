# Trabalho Prático de Banco de Dados
Professor: André Britto de Carvalho

# Aplicação
A parte 4 terá duas etapas.

## Primeira etapa
Implementar um programa em qualquer linguagem de programação escolhida pelo
grupo que faz a comunicação com o SGBD. O programa deve se conectar ao SGBD
criado na parte 3 do trabalho prático. Além disso, deve ter dois métodos, um método
para inserir uma linha e outro para consultar alguma tabela escolhida pelo grupo.
Nessa etapa não deve ser usado nenhum framework de desenvolvimento. O código
deve ser executado localmente e as consultas devem estar explícitas nos métodos.
Será criada uma tarefa no SIGAA e basta enviar o código-fonte.

## Segunda etapa
A segunda etapa da parte 4 consiste na API Web que efetua o CRUD (insert,delete,
update e leitura) de três tabelas do banco de dados, sendo duas tabelas geradas a
partir de entidades e uma tabela gerada a partir de um relacionamento ou
agregação.
A aplicação desenvolvida não representa a aplicação descrita na especificação.
Essa etapa tem como objetivo o desenvolvimento de um programa que se comunica
com um SGBD e executa operações de manipulação de dados.
Nesta etapa, é necessário enviar o código fonte idealmente através de um projeto
no github ou ferramenta similar. O grupo deve gravar um vídeo mostrando o
funcionamento de todas as rotas. Para cada rota, é necessário mostrar o efeito dela
no banco de dados. A avaliação da aplicação será através do vídeo, assim fiquem
atentos que todas as operações implementadas devem ser apresentadas no vídeo.

## Atividade extra
O grupo poderá ganhar 0,5 ponto extra na nota da unidade. A atividade consiste em
implementar um método que efetue uma transação. Esse método deve obrigatoriamente
fazer uma operação de consulta e uma operação de inserção/atualização. Esse método
também deve estar disponível na API Web.