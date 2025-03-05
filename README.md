CRUD de Usuários

Este projeto é simples, um sistema de CRUD (Create, Read, Update, Delete) para gerenciamento de usuários. O sistema permite cadastrar, listar, buscar, atualizar e excluir usuários em um banco de dados MySQL.

Funcionalidades

Cadastrar Usuário: Adicionar um novo usuário com nome, e-mail e telefone
Listar Usuários: Exibir todos os usuários cadastrados no sistema
Buscar Usuário: Procurar um usuário pelo nome
Atualizar Usuário: Alterar os dados de um usuário existente
Excluir Usuário: Remover um usuário do sistema

A parte estrutural fiz por conta própria usando as documentações e oque já sabia
A biblioteca rich foi toda openai, para melhor compreensão do usuario(so sei usar o collorama :) )

tempo de codigo(2 horas e 23 minutos)  ;)



USE -

cd crud-usuarios
//
python -m venv .venv (Ambiente faz, se quiser)
.venv\Scripts\activate (Windows)
//
pip install -r requirements.txt
//
IN MYSQL

CREATE DATABASE usuarios_db;
USE usuarios_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20)
);
//
python crud.py

---------------------------------------------------------------------------------------------------------------------------------------------------


User CRUD

This project is simple, a CRUD (Create, Read, Update, Delete) system for user management. The system allows you to create, list, search, update, and delete users in a MySQL database.

Features

Create User: Add a new user with name, email, and phone number  
List Users: Display all users registered in the system  
Search User: Search for a user by name  
Update User: Change the data of an existing user  
Delete User: Remove a user from the system

The structural part I did on my own using the documentation and what I already knew  
The rich library was all OpenAI's, for better user comprehension (I only know how to use Collorama)

Time spent coding: 2 hours and 23 minutes ;)

---------------------------------------------------

USE 

cd crud-usuarios  
//  
python -m venv .venv (Environment setup, if you want)  
.venv\Scripts\activate (Windows)  
//  
pip install -r requirements.txt  
//  
IN MYSQL  

CREATE DATABASE usuarios_db;  
USE usuarios_db;  

CREATE TABLE usuarios (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    nome VARCHAR(100),  
    email VARCHAR(100),  
    telefone VARCHAR(20)  
);  
//  
python crud.py  




