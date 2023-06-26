import sqlite3

class Model:
    def __init__(self):
        self.conector = None
        self.curso = None
        self.conectar()
        self.criar_tabela_fornecedores()

    def conectar(self):
        self.conector = sqlite3.connect("Cadastro.bd")
        self.curso = self.conector.cursor()

    def desconectar(self):
        self.conector.close()

    def criar_tabela_fornecedores(self):
        self.curso.execute("""
            CREATE TABLE IF NOT EXISTS contatos (
                ID INTEGER PRIMARY KEY,
                name CHAR(40) NOT NULL,
                phone INTEGER(20) NOT NULL,
                CNPJ CHAR(40) NOT NULL,
                Type CHAR(40),
                fav CHAR(20)
            );
        """)
        self.conector.commit()

    def lista_vil(self):
        self.conectar()
        self.curso.execute("""SELECT ID, name, phone, CNPJ, Type, fav FROM contatos ORDER BY ID ASC""")
        contatos = self.curso.fetchall()
        self.desconectar()
        return contatos

    def add_pessoa(self, name, phone, CNPJ, Type, fav):
        self.conectar()
        self.curso.execute("""INSERT INTO contatos (name, phone, CNPJ, Type, fav) VALUES (?, ?, ?, ?, ?)""", (name, phone, CNPJ, Type, fav))
        self.conector.commit()
        self.desconectar()

    def delete_pessoa(self, id):
        self.conectar()
        self.curso.execute("""DELETE FROM contatos WHERE ID = ?""", (id,))
        self.conector.commit()
        self.desconectar()

    def alt_pessoa(self, id, name, phone, CNPJ, Type, fav):
        self.conectar()
        self.curso.execute("""UPDATE contatos SET name = ?, phone = ?, CNPJ= ?, Type = ?, fav = ? WHERE ID = ?""",
                           (name, phone, CNPJ, Type, fav, id))
        self.conector.commit()
        self.desconectar()

    def search_pessoa(self, name):
        self.conectar()
        contatos = self.curso.execute("""SELECT ID, name, phone, CNPJ, Type, fav FROM contatos WHERE name LIKE ? ORDER BY name ASC""",
                                      ('%' + name + '%',))
        self.desconectar()
        return contatos

    def close_connection(self):
        self.conexao.close()