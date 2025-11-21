# 📘 Assignment: Construindo APIs REST com framework FastAPI

## 🎯 Objetivo

Aprender a construir APIs REST utilizando o framework FastAPI. Os estudantes irão criar endpoints básicos, configurar rotas e trabalhar com validação de dados.

## 📝 Tarefas

### 🛠️ Criar um endpoint GET

#### Descrição
Crie um endpoint GET que retorne uma mensagem de boas-vindas.

#### Requisitos
O programa deve:

- Responder na rota `/` com uma mensagem de boas-vindas.
- Utilizar o método GET.
- Retornar um JSON com a mensagem.

### 🛠️ Criar um endpoint POST

#### Descrição
Crie um endpoint POST que receba dados de um usuário e retorne uma mensagem de confirmação.

#### Requisitos
O programa deve:

- Responder na rota `/users`.
- Aceitar um JSON com os campos `name` e `age`.
- Retornar um JSON confirmando o recebimento dos dados.

### 🛠️ Criar validação de dados

#### Descrição
Adicione validação para garantir que o campo `age` seja um número maior que 0.

#### Requisitos
O programa deve:

- Retornar um erro 422 se o campo `age` for inválido.
- Utilizar o recurso de validação do Pydantic.