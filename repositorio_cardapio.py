import sqlite3

class RepositorioCardapio:
    def __init__(self, nome_bd) -> None:
        self.nome_bd = nome_bd
        self.conexao = None
        self.cursor= None
        
    def open_conn(self):
        self.conexao = sqlite3.connect('bd.sqlite') 
        self.cursor = self.conexao.cursor()
        
    def close_conn(self):
        self.cursor.close()
        self.conexao.close()    
        self.conexao = None
        self.cursor = None 

# ABAIXO FAREMOS O CRUD EM CARDAPIOS ----------------------------------- 

# CRIAR----------------------------------------------------------------
# CRIAR CARDAPIO ------------------------------------------------------
    def criar_cardapio(self, codigo:str, nome:str, descricao:str)-> None:
        self.open_conn()
        # CRIEI UMA VARIAVEL PARA RECEBER O SQL - (CODE)
        query_code ='INSERT OR IGNORE INTO cardapios(codigo,nome,descricao) VALUES(?,?,?)'
        self.cursor.execute(query_code,(codigo, nome, descricao)) 
        self.conexao.commit()
        
        self.close_conn()

# CONSULTAR--------------------------------------------------------------
# CONSULTAR CARDAPIO-----------------------------------------------------
    def consultar_cardapios(self)-> list:
        self.open_conn()
        query_code = 'SELECT * FROM cardapios;'
        self.cursor.execute(query_code)
        leitura = self.cursor.fetchall()
             
        self.close_conn()
        return leitura

# CONSULTAR APENAS 1 ELEMENTO DO CARDAPIO -----------------------------------    
    def consultar_elemento_cardapios(self, codigo:str)-> tuple:
        self.open_conn()
        query_code = 'SELECT * FROM cardapios WHERE codigo = ?;'
        self.cursor.execute(query_code,(codigo,))    
        leitura = self.cursor.fetchone()
        
        self.close_conn()
        return leitura   

#UPDATE ------------------------------------------------------------------
# ATUALIZAR CARDAPIO -----------------------------------------------------    
    def atualizar_cardapios(self, codigo:str, nome:str, descricao:str) -> None:  
        self.open_conn()
        query_code = 'UPDATE cardapios SET codigo = ?, nome = ?, descricao = ? WHERE codigo = ?;'
        self.cursor.execute(query_code,(codigo,nome,descricao, codigo))
        self.conexao.commit()
        
        self.close_conn()
    
# DELETAR -----------------------------------------------------------------
     
    def deletar_cardapios(self, codigo:str)-> None:
        self.open_conn()
        query_code = 'DELETE FROM cardapios WHERE codigo = ?'
        self.cursor.execute(query_code,(codigo,))
        self.conexao.commit()
            
        self.close_conn()

    
