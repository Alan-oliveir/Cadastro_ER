import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabelas
def create_basic():
    with con:
        cur = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Embaixador'"
        list_table = cur.execute(query).fetchall()
        if list_table == []:
            cur.execute("CREATE TABLE Embaixador (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_ER TEXT, nome_resp TEXT, data_nasc DATE, tel_resp TEXT, tel_ER TEXT, cep INTEGER, logradouro TEXT, numero INTEGER, bairro TEXT, cidade TEXT, estado TEXT, complemento TEXT, image TEXT)")

def create_church():
    with con:
        cur = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Igreja'"
        list_table = cur.execute(query).fetchall()
        if list_table == []:
            cur.execute("CREATE TABLE Igreja (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_ER TEXT, nome_igreja TEXT, igreja_batismo TEXT, data_batismo DATE, EBD TEXT, atividades TEXT)")

def create_org():
    with con:
        cur = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Organizacao'"
        list_table = cur.execute(query).fetchall()
        if list_table == []:
            cur.execute("CREATE TABLE Organizacao (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_ER TEXT, ingresso DATE, aclamacao DATE, posto TEXT, formatura DATE, observacao TEXT)")

# Inserir dados do ER 
def inserir_form(i):
    create_basic()
    with con:
        cur = con.cursor()
        query = "INSERT INTO Embaixador (nome_ER, nome_resp, data_nasc, tel_resp, tel_ER, cep, logradouro, numero, bairro, cidade, estado, complemento, image) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

# Inserir dados da igreja
def inserir_church(i):
    create_church()
    with con:
        cur = con.cursor()
        query = "INSERT INTO Igreja (nome_ER, nome_igreja, igreja_batismo, data_batismo, EBD, atividades) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)

# Inserir dados do ER na organização
def inserir_org(i):
    create_org()
    with con:
        cur = con.cursor()
        query = "INSERT INTO Organizacao (nome_ER, ingresso, aclamacao, posto, formatura, observacao) VALUES (?,?,?,?,?,?)"
        cur.execute(query, i)
