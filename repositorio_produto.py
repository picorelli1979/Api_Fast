import sqlite3
from dtos import ProdutoOut
from typing import List

class RepositorioProduto:
    
    def montar(self, tupla_dados: tuple) -> ProdutoOut:
        codigo, codigo_cardapio, nome, descricao, preco, restricao = tupla_dados
        preco = float(preco)
        return ProdutoOut(codigo=codigo, codigo_cardapio=codigo_cardapio, 
            nome=nome, descricao=descricao, preco=preco, restricao=restricao)
    
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
  
# ABAIXO FAREMOS O CRUD EM PRODUTOS ----------------------------------- 

# CRIAR----------------------------------------------------------------
    def criar_produto(self, codigo:str, nome:str, descricao:str, valor: float, restricao:str, codigo_cardapio:str )-> None:
        self.open_conn()
        # CRIEI UMA VARIAVEL PARA RECEBER O SQL - (CODE)
        query_code ='INSERT OR IGNORE INTO produtos(codigo,nome,descricao, preco, restricao, codigo_cardapio) VALUES(?,?,?)'
        self.cursor.execute(query_code,(codigo, nome, descricao, valor, restricao, codigo_cardapio)) 
        self.conexao.commit()
        
        self.close_conn()

# CONSULTAR--------------------------------------------------------------
    # def consultar_produto(self)-> list:
    #     self.open_conn()
    #     query_code = 'SELECT * FROM produtos;'
    #     self.cursor.execute(query_code)
    #     leitura = self.cursor.fetchall()
    
    #     self.close_conn()
    #     return leitura
    
    def consultar_produto(self, preco_min: int = -1, preco_max: int = 99999, 
        codigo_cardapio: str = '', restricao: str = '') -> List[ProdutoOut]:
        
        query = 'SELECT codigo,codigo_cardapio,nome,descricao,preco,restricao FROM produto WHERE preco >= ? AND preco <= ?'

        parametros = [preco_min, preco_max]

        if codigo_cardapio:
            query += ' AND codigo_cardapio = ?'
            parametros.append(codigo_cardapio)

        if restricao:
            query += ' AND restricao = ?'
            parametros.append(restricao)

        query += ';'
        
        self.open_conn()
        self.cursor.execute(query, tuple(parametros))
        produtos = self.cursor.fetchall()
        self.close_conn()
        return [self.montar(produto) for produto in produtos]


    def consultar_elemento_produto(self, codigo:str)-> tuple:
        self.open_conn()
        query_code = 'SELECT * FROM produtos WHERE codigo = ?;'
        self.cursor.execute(query_code,(codigo,))    
        leitura = self.cursor.fetchone()
        
        self.close_conn()
        return self.montar(leitura)   

#UPDATE ------------------------------------------------------------------
    
    def atualizar_produto(self, codigo:str, nome:str, descricao:str, codigo_cardapio:str, valor:float, restricao:str) -> None:  
        self.open_conn()
        query_code = 'UPDATE produtos SET codigo = ?, nome = ?, descricao = ?, codigo_cardapio =?, preco = ?, restricao = ? WHERE codigo = ?;'
        self.cursor.execute(query_code,(codigo,nome,descricao, codigo_cardapio, valor, restricao, codigo))
        self.conexao.commit()
        
        self.close_conn()
    
# DELETAR -----------------------------------------------------------------
     
    def deletar_produto(self, codigo:str)-> None:
        self.open_conn()
        query_code = 'DELETE FROM produtos WHERE codigo = ?'
        self.cursor.execute(query_code,(codigo,))
        self.conexao.commit()
            
        self.close_conn()

    
      