<h1 align="center"> 
  <a href="#" alt="CRUD Usuários API">👤 CRUD Usuários API</a> 
</h1>

<h2>Contents</h2>

- [1. About 💻](#1-about-)
- [2. API Documentation 💾](#2-api-documentation-)
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
- [6 - Endpoints 🔗](#6---endpoints-)
	- [LISTAR TODOS OS USUÁRIOS](#listar-todos-os-usuários)
	- [LISTAR UM USUÁRIO PELO ID](#listar-um-usuário-pelo-id)
	- [CRIAR UM NOVO USUÁRIO](#criar-um-novo-usuário)
	- [MODIFICAR UM USUÁRIO JÁ CADASTRADO](#modificar-um-usuário-já-cadastrado)
	- [DELETAR UM USUÁRIO EXISTENTE](#deletar-um-usuário-existente)
- [7 - FILTROS 📄](#7---filtros-)
- [8 - PAGINAÇÃO 📙](#8---paginação-)
- [9 - TERMOS DE USO 📜](#9---termos-de-uso-)

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

## 2. API Documentation 💾

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

## 6 - Endpoints 🔗

### LISTAR TODOS OS USUÁRIOS

    Método GET

    ENDPOINT: baseURL/users

    


### LISTAR UM USUÁRIO PELO ID

    Método GET

    ENDPOINT: baseURL/users/{user_id}

   

### CRIAR UM NOVO USUÁRIO

    Método POST

    ENDPOINT: baseURL/users

	


### MODIFICAR UM USUÁRIO JÁ CADASTRADO

	Método PATCH

	ENDPOINT: baseURL/users/{user_id}

	

### DELETAR UM USUÁRIO EXISTENTE

	Método DELETE

	ENDPOINT: baseURL/users/{user_id}

	


## 7 - FILTROS 📄

	Pode-se filtrar o resultado da listagem de todos os usuários por nome e/ou por email.

	Deve-se montar o endpoint como informado abaixo:

	baseURL/users?name=NOMEBUSCADO&email=EMAILBUSCADO

	O resultado, caso sejam encontrados usuários onde os dados atendam aos critérios de busca, será uma listagem de objetos usuário.
	Caso nenhum dados seja encontrado no banco de dados nada será retornado.

## 8 - PAGINAÇÃO 📙 

	A paginação é feita de forma semelhante ao filtro, conforme indicado abaixo:

	baseURL/users?page=12

	Observe que ao final de cada lista, são exibidas algumas informações sobre os dados.

	"total": 150         - quantidade de objetos (usuários) na tabela
	"page": 14           - número da página atual
	"size": 10           - número de objetos (usuários) exibidos
	"total_pages": 15    - número total de páginas
	"has_next": true     - se existe uma nova página
	"has_previous": true - se existe uma página anterior

## 9 - TERMOS DE USO 📜

Este é um projeto open source para uso educacional e não comercial.


**Tipo de licença**:  <a name="gpl" href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GPL</a>


