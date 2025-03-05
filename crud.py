from database import conectar
from time import sleep

def inserir_usuario(nome, email, telefone):
    conn = conectar()
    cursor = conn.cursor()
    query = "INSERT INTO usuarios (nome, email, telefone) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, email, telefone))
    conn.commit()
    cursor.close()
    conn.close()
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}")

def buscar_usuario(nome):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome LIKE %s"
    cursor.execute(query, (f"%{nome}%",))
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}")
    else:
        print("Usuário não encontrado.")

def atualizar_usuario(id, nome, email, telefone):
    conn = conectar()
    cursor = conn.cursor()
    query = "UPDATE usuarios SET nome = %s, email = %s, telefone = %s WHERE id = %s"
    cursor.execute(query, (nome, email, telefone, id))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Usuário com ID {id} atualizado com sucesso!")

def excluir_usuario(id):
    conn = conectar()
    cursor = conn.cursor()
    query = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Usuário com ID {id} excluído com sucesso!")
