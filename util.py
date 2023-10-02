import unicodedata
from pydantic import SecretStr

class Utilidades:
    @staticmethod
    def criar_codigo(nome:str) -> str:
        #CONVERTER PARA MINUSCULAS 
        nome = nome.lower()
        
        # REMOVER OS ACENTOS 
        nome = ''.join(c for c in unicodedata.normalize('NFKD', nome)
                       if unicodedata.category(c) != 'Mn')

        #REMOVER TODOS OS CARACTERES QUE NÃO SÃO LETRAS, NÚMEROS OU ESPAÇOS
        nome = ''.join(c for c in nome if c.isascii() and (c.isalnum() or c == ' '))
         
        #TROCAR ESPAÇOS POR TRAÇOS 
        nome = nome.replace(' ', '-')
        
        return nome 
         
    @staticmethod
    def is_alnum_hyphen(texto:str) ->str:
        for c in texto:
            if not c.isalnum()and c != '-':
                raise ValueError
        return texto
    
    @staticmethod
    def is_alpha_dot(texto:str) ->str:
        for c in texto:
            if not c.isalpha()and c != '.':
                raise ValueError
        return texto
    
    @staticmethod
    def is_alpha_space(texto:str) ->str:
        for c in texto:
            if not c.isalpha()and c != ' ':
                raise ValueError
        return texto
     
    @staticmethod
    def validar_senha(senha:SecretStr)->SecretStr:
        for c in senha.get_secret_value():
            if not c.isalnum()and c not in '._?!@$#&*+':
                raise ValueError
        return senha
    
    
    
    
    