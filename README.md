# apy_Crud_aluno
# APy de Alunos - Flask

Este projeto consiste no desenvolvimento de uma API REST utilizando Python e o framework Flask, com o objetivo de realizar operações CRUD (Create, Read, Update e Delete) para a entidade Aluno.

Os dados são armazenados em um arquivo JSON (`alunos.json`), funcionando como uma base de dados simples.

**Objetivo**

Atender aos requisitos da atividade prática da disciplina Programação para Web I, implementando uma API funcional com manipulação de dados via arquivo JSON.


## Tecnologias utilizadas

* Python
* Flask
* JSON
* Postman (para testes)


## Estrutura do projeto

apy-alunos/
app.py → Arquivo principal da API
alunos.json → Base de dados (JSON)
README.md → Documentação
models/
  init.py
  aluno.py → Classe Aluno



## Como executar a aplicação

### 1. Instalar o Flask

No terminal, execute:

bash
pip install flask

### 2. Executar o projeto

bash
python app.py


### 3. Acessar a API

A API estará disponível em:

http://127.0.0.1:5000

---

## Testando a API no Postman

Utilize o Postman para testar as rotas:



### 1. Criar aluno (CREATE)

* Método: **POST**
* URL: http://127.0.0.1:5000/alunos

Body → raw → JSON:

  json
{
  "nome": "Adriel",
  "curso": "ADS",
  "idade": 22
}



### 2. Listar alunos (READ)

* Método: **GET**
* URL: http://127.0.0.1:5000/alunos



### 3. Buscar aluno por matrícula (READ)

* Método: **GET**
* URL: http://127.0.0.1:5000/alunos/1



### 4. Atualizar aluno (UPDATE)

* Método: **PUT**
* URL: http://127.0.0.1:5000/alunos/1

Body → JSON:

 json
{
  "curso": "Desenvolvimento de sistema"
}

###  5. Deletar aluno (DELETE)

* Método: **DELETE**
* URL: http://127.0.0.1:5000/alunos/1



## Estrutura do JSON

Os dados são armazenados no arquivo `alunos.json` no seguinte formato:
 json

    {
        "matricula": 1,
        "nome": "Adriel",
        "idade": 22,
        "curso": "ADS"
    }


## Observações importantes

* O arquivo `alunos.json` deve existir e iniciar com:

  json
[]

* Sempre selecionar **Body → raw → JSON** no Postman
* O servidor Flask deve estar em execução
* Os dados são persistidos no arquivo JSON



## Funcionalidades da API

*  Cadastrar aluno
*  Listar alunos
*  Buscar aluno por matrícula
*  Atualizar dados do aluno
*  Remover aluno

## Considerações finais

Este projeto demonstra a implementação de uma API REST simples utilizando Flask, com persistência de dados em arquivo JSON, atendendo aos requisitos propostos na atividade acadêmica.
