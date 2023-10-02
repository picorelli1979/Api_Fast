import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from bcrypt import gensalt, hashpw

class Autenticador(object):
    
    def __init__(self, algoritmo_chave: str, chave_privada:str, chave_publica:str, 
       validade_token: int = 60, custo_salt:int = 12)-> None:
       self.algoritmo_chave = algoritmo_chave
       self.chave_privada = chave_privada
       self.chave_publica = chave_publica
       self.validade_token = validade_token
       self.custo_salt = custo_salt
        
    def gerar_salt(self) -> bytes:
        return gensalt(self.custo_salt)
    
    def gerar_hash_senha(self, salt:bytes, senha:str) -> bytes:
        return hashpw(bytes(senha, encoding='utf8'), salt)
    
    def gerar_token_jwt(self, dados: dict, validade_minutos: int = 0)->str:   
    
        if validade_minutos == 0:
           validade_minutos = self.validade_token 
        iat = datetime.now(timezone.utc)
        exp = iat + timedelta(minutes=validade_minutos)
        dados.update({'iat':iat, 'exp':exp})
        token = jwt.encode(dados, self.chave_privada, self.algoritmo_chave)
        return token 
    
    def validar_token_jwt(self, token:str)-> dict | None:
        try:
            dados = jwt.decode(token, self.chave_publica,self.algoritmo_chave, 
                options = {"require":["iat", "exp"]})
                
            now = datetime.timestamp(datetime.now(timezone.utc))
            if now < dados['iat'] or now > dados['exp']:
                return None
                
            return dados 
            
        except InvalidTokenError:
            return None 