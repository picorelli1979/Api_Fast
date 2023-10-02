import sqlite3
from dtos import Usuario 

class RepositorioUsuario:
    
    FOREIGN_KEY_SQLITE = 'PRAGMA foreign_keys=ON;'
    LINHAS_AFETADAS_SQLITE = 'SELECT changes();'
    
    @staticmethod
    def montar(tupla_dados:tuple)-> Usuario:
        nome_usuario, nome_completo, cargo = tupla_dados
        return Usuario(nome_usuario=nome_usuario, nome_completo = nome_completo, cargo = cargo)
    
    def __init__(self, nome_db:str)-> None:
        self.nome_db = nome_db
        self.conexao = None
        self.cursor = None
      
    def open_conn(self):
        self.conexao = sqlite3.connect('bd.sqlite') 
        self.cursor = self.conexao.cursor()
        self.ativar_foreign_key()
        
    def close_conn(self):
        self.cursor.close()
        self.conexao.close()    
        self.conexao = None
        self.cursor = None  
    
    def ativar_foreign_key(self) -> None:
        self.cursor.execute(self.FOREIGN_KEY_SQLITE)
    
    def obter_mudancas(self)->int :
        mudancas = self.cursor.execute(self.LINHAS_AFETADAS_SQLITE)
        return mudancas.fetchone()[0]
    
    def obter_mudancas_fechar(self)->int :            
        mudancas = self.obter_mudancas()
        self.close_conn()
        return mudancas
    
    def criar(self, nome_usuario:str, nome_completo:str, cargo:str, salt_senha:bytes, hash_senha:bytes)->int :
        query ='INSERT OR IGNORE INTO usuario(nome_usuario,nome_completo,cargo,salt_senha, hash_senha) VALUES (?,?,?,?,?);'
        self.open_conn()
        self.cursor.execute(query,(nome_usuario,nome_completo,cargo,salt_senha,hash_senha))
        self.conexao.commit()
        return self.obter_mudancas_fechar()
    
    def consultar(self, nome_usuario:str) -> Usuario:
        query ='SELECT nome_usuario, nome_completo, cargo FROM usuario WHERE nome_usuario =?;'
        self.open_conn()
        self.cursor.execute(query,(nome_usuario,))
        usuario = self.cursor.fetchone()
        self.close_conn()
        return self.montar(usuario) if usuario else None
    
    def consultar_salt(self, nome_usuario:str)->bytes:
        query = 'SELECT salt_senha FROM usuario WHERE nome_usuario =?;'
        self.open_conn()
        self.cursor.execute(query,(nome_usuario,))
        salt = self.cursor.fetchone()
        self.close_conn()
        return salt[0] if salt else None
     
    def consultar_credencias(self, nome_usuario:str, salt_senha:bytes,hash_senha:bytes)->Usuario:
        query = 'SELECT nome_usuario,nome_completo,cargo FROM usuario WHERE nome_usuario=? AND salt_senha=? AND hash_senha=?;'
        self.open_conn()
        self.cursor.execute(query,(nome_usuario, salt_senha, hash_senha))
        usuario = self.cursor.fetchone()
        self.close_conn()
        return self.montar(usuario) if usuario else None      
    
    
    
    
    
    
    
    
    
    
    
    
    
    