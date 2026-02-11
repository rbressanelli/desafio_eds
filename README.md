<h1 align="center"> 
  <a href="#" alt="CRUD Usuários API">👤 CRUD Usuários API</a> 
</h1>

<h2>Contents</h2>

- [1. About 💻](#1-about-)
- [2. API Documentation 🔗](#2-api-documentation-)
- [3. Technologies 🧰](#3-technologies-)
- [4. Requirements ☑️](#4-requirements-️)
- [5. Running the Application ▶️](#5-running-the-application-️)
	- [1 – Clone o repositório](#1--clone-o-repositório)
	- [2 – Criar ambiente virtual](#2--criar-ambiente-virtual)
	- [3 – Ativar ambiente virtual](#3--ativar-ambiente-virtual)
	- [4 – Instalar pacotes de dependências](#4--instalar-pacotes-de-dependências)
	- [5 – Ativar o contêiner do banco de dados](#5--ativar-o-contêiner-do-banco-de-dados)
	- [6 – Executar migrações](#6--executar-migrações)
	- [7 – Iniciar a API](#7--iniciar-a-api)
	- [8 - URL base de acesso à API](#8---url-base-de-acesso-à-api)
- [6 - Endpoints](#6---endpoints)
	- [LISTAR TODOS OS USUÁRIOS](#listar-todos-os-usuários)
	- [LISTAR UM USUÁRIO PELO ID](#listar-um-usuário-pelo-id)
	- [CRIAR UM NOVO USUÁRIO](#criar-um-novo-usuário)
	- [MODIFICAR UM USUÁRIO JÁ CADASTRADO](#modificar-um-usuário-já-cadastrado)
	- [DELETAR UM USUÁRIO EXISTENTE](#deletar-um-usuário-existente)
- [7 - FILTROS](#7---filtros)
- [8 - PAGINAÇÃO](#8---paginação)

---

<a name="about"></a>

## 1. About 💻

Este projeto consiste em uma **API CRUD simples de usuários**, permitindo:

- Cadastrar usuários  
- Listar usuários  
- Atualizar usuários  
- Deletar usuários  

A aplicação foi desenvolvida utilizando **Python + FastAPI**.

O banco de dados utilizado é **PostgreSQL**, executado em um **contêiner Docker (Postgres 18.1-alpine)**.

- 🔎 Validações e tratamento de erros: **Pydantic**
- 🔄 Gerenciamento de migrações: **Alembic**

---

<a name="documentation"></a>

## 2. API Documentation 🔗

A documentação interativa (Swagger) pode ser acessada em:

<a href="http://127.0.0.1:8000/docs" target="_blank">Documentação => Swagger</a>

---

<a name="technologies"></a>

## 3. Technologies 🧰

- <a href="https://www.python.org/" target="_blank">Python 3.13+</a>  
- <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a>  
- <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a>  
- <a href="https://www.docker.com/" target="_blank">Docker</a>  
- <a href="https://alembic.sqlalchemy.org/" target="_blank">Alembic</a>  
- <a href="https://docs.pydantic.dev/" target="_blank">Pydantic</a>  
- Uvicorn  

---

<a name="requirements"></a>

## 4. Requirements ☑️

É necessário ter instalado na máquina:

- Python 3.13+  
- Docker / Docker Desktop  

---

<a name="running"></a>

## 5. Running the Application ▶️

### 1 – Clone o repositório

```bash
git clone <url-do-repositorio>
```

### 2 – Criar ambiente virtual
```bash
python -m venv venv
```
⚠️ Dependendo de sua máquina, o comando pode ser python3.

### 3 – Ativar ambiente virtual

Linux / MacOS
```bash
source venv/bin/activate
```

Windows
```bash
.\venv\Scripts\activate
```
⚠️ Certifique-se de que o ambiente virtual está ativado antes de continuar.

### 4 – Instalar pacotes de dependências
```bash
pip install -r requirements.txt
```

### 5 – Ativar o contêiner do banco de dados
```bash
docker compose up
```

### 6 – Executar migrações
```bash
alembic upgrade head
```
### 7 – Iniciar a API
```bash
uvicorn main:app
```
### 8 - URL base de acesso à API
```bash
http://127.0.0.1:8000/api/v1
```

## 6 - Endpoints

### LISTAR TODOS OS USUÁRIOS

    Método GET
    baseURL/users

    Resposta esperada: 200 - OK
	{
	"items": [
		{
			"name": "Name142",
			"surname": "Surname142",
			"email": "user142@example.com",
			"age": 38,
			"id": 142
		},
		{
			"name": "Name143",
			"surname": "Surname143",
			"email": "user143@example.com",
			"age": 56,
			"id": 143
		},
		...parte do conteúdo foi suprimido
				},
		{
			"name": "Roberto",
			"surname": "Bressanelli",
			"email": "email@emai.com",
			"age": 56,
			"id": 151
		}
	],
	"total": 150,
	"page": 1,
	"size": 10,
	"total_pages": 15,
	"has_next": true,
	"has_previous": false
	}
   

    Resposta esperada se não existirem dados no banco: 200 - OK
    [] - lista vazia


### LISTAR UM USUÁRIO PELO ID

    Método GET
    baseURL/users/{user_id}

    Resposta esperada: 200 - OK

	[
		{
		"name": "Roberto",
		"surname": "Bressanelli",
		"email": "email@email.com",
		"age": 34,
		"id": 1
		}
	]
    
    Resposta no caso  de usuário inexistente:
	404 – Not Found
   
	{
	  "detail": "Usuário não encontrado"
	}


### CRIAR UM NOVO USUÁRIO

    Método POST
    baseURL/users

	Exemplo de corpo de requisição:

	{
		"name": "Roberto",
		"surname": "Bressanelli",
		"email": "email@email.com",
		"age": 34
	}  

	Resposta esperada em caso de sucesso: 201 – Created

	{
		"name": "Roberto",
		"surname": "Bressanelli",
		"email": "email@email.com",
		"age": 34,
		"id": 2
	} 

	Resposta caso já exista o mesmo e-mail cadastrado: 409 – Conflict

	{
		"detail": "Email já cadastrado"
	}

	Resposta esperada caso insira um valor inválido para idade (texto ou float)
	422 – Unprocessable Content

	{
	"detail": [
		{
			"type": "int_from_float",
			"loc": [
				"body",
				"age"
				],
				"msg": "Input should be a valid integer, got a number with a fractional part",
				"input": 22.5
			}
		]
	}


	Respostas no caso de umail inválido: 422 – Unprocessable Content

	{
	"detail": [
		{
			"type": "value_error",
			"loc": [
				"body",
				"email"
				],
				"msg": "value is not a valid email address: The part after the @-sign is not valid. It should have a period.",
				"input": "email@emai",
				"ctx": {
				"reason": "The part after the @-sign is not valid. It should have a period."
				}
			}
		]
	}


	{
	"detail": [
		{
			"type": "value_error",
			"loc": [
				"body",
				"email"
				],
				"msg": "value is not a valid email address: An email address must have an @-sign.",
				"input": "emailemail.com",
				"ctx": {
				"reason": "An email address must have an @-sign."
				}
			}
		]
	}


### MODIFICAR UM USUÁRIO JÁ CADASTRADO

	Método PATCH
	baseURL/users/{user_id}

	OBS: Pode ser modificado um ou vários atributos na mesma request.


	Exemplo de corpo de requisição:
	{
		“age”: 45
	}

	Resposta esperada no caso de sucesso: 202 – Accepted

	{
		"name": "Roberto",
		"surname": "Bressanelli",
		"email": "email@email.com",
		"age": 45,
		"id": 2
	}

	Resposta no caso  de usuário inexistente: 404 – Not Found

	{
		"detail": "Usuário não encontrado"
	}

	Resposta caso já exista o mesmo e-mail cadastrado: 409 – Conflict

	{
		"detail": "Email já cadastrado"
	}	

	Respostas possíveis para e-mails inválidos:	422 – Unprocessable Content

	Ver respostas no campo de criar usuário.

### DELETAR UM USUÁRIO EXISTENTE

	Método DELETE
	baseURL/users/{user_id}

	Resposta esperada em caso de sucesso: 204 – No Content
	Sem corpo de retorno.

	Resposta no caso  de usuário inexistente: 404 – Not Found

	{
		"detail": "Usuário não encontrado"
	}


## 7 - FILTROS

	Pode-se filtrar o resultado da listagem de todos os usuários por nome e/ou por email.

	Deve-se montar o endpoint como informado abaixo:

	baseURL/users?name=NOMEBUSCADO&email=EMAILBUSCADO

	O resultado, caso sejam encontrados usuários onde os dados atendam aos critérios de busca, será uma listagem de objetos usuário.
	Caso nenhum dados seja encontrado no banco de dados nada será retornado.

## 8 - PAGINAÇÃO

	A paginação é feita de forma semelhante ao filtro, conforme indicado abaixo:

	baseURL/users?page=12

	Observe que ao final de cada lista, são exibidas algumas informações sobre os dados.

	"total": 150         - quantidade de objetos (usuários) na tabela
	"page": 14           - número da página atual
	"size": 10           - número de objetos (usuários) exibidos
	"total_pages": 15    - número total de páginas
	"has_next": true     - se existe uma nova página
	"has_previous": true - se existe uma página anterior

