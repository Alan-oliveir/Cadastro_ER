import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
def create():
    with con:
        cur = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Embaixador'"
        list_table = cur.execute(query).fetchall()
        if list_table == []:
            cur.execute("CREATE TABLE Embaixador (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_ER TEXT, nome_resp TEXT, data_nasc DATE, tel_resp TEXT, tel_ER TEXT, cep INTEGER, logradouro TEXT, numero INTEGER, bairro TEXT, cidade TEXT, estado TEXT, complemento TEXT, image TEXT)")

# Inserir
def inserir_form(i):
    create()
    with con:
        cur = con.cursor()
        query = "INSERT INTO Embaixador (nome_ER, nome_resp, data_nasc, tel_resp, tel_ER, cep, logradouro, numero, bairro, cidade, estado, complemento, image) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

''' Funções a serem implementadas no arquivo visualizar_ER.py
# Ver Inventario
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()        
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Atualizar inventorio
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?, valor_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)

# Deletar inventorio
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query, i)'''
