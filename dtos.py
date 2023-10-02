from pydantic import BaseModel, Field, validator, SecretStr
from typing import Literal 
from util import Utilidades

class CardapioOut(BaseModel):
    codigo: str = Field(min_length=2, max_length=50)
    nome : str = Field(min_length=2, max_length=50)
    descricao : str = Field(max_length=255)
    
    @validator('codigo')
    def validar_codigo(codigo:str) -> str:
        return Utilidades.is_alnum_hyphen(codigo)
    
class CardapioIn(BaseModel):
    nome: str = Field(min_length=2, max_length=50)
    decricao: str = Field(max_length=255)

class DescricaoCardapio(BaseModel):
    descricao: str = Field(max_length=255) 
    
class ProdutoOut(BaseModel):
    codigo: str = Field(min_length=2,max_length=50)
    codigo_cardapio: str = Field(min_length=2,max_length=50)
    nome: str = Field(min_length=2,max_length=50)
    descricao: str = Field(min_length=2,max_length=255)
    valor: float = Field(ge=0)
    restricao: str = Field(min_length=2,max_length=20)
    
    @validator('codigo','codigo_cardapio')
    def validar_codigo(codigo:str) -> None:
        return Utilidades.is_alnum_hyphen(codigo)
    
class ProdutoIn(BaseModel):
    codigo_cardapio: str = Field(min_length=2,max_length=50)
    nome: str = Field(min_length=2,max_length=50)
    descricao: str = Field(min_length=2,max_length=255)
    valor: float = Field(ge=0)
    restricao: str = Field(min_length=2,max_length=20)
    
    @validator('codigo_cardapio')
    def validar_codigo(codigo:str) -> None:
        return Utilidades.is_alnum_hyphen(codigo)   
    
class PrecoProduto(BaseModel):
    valor: float = Field(ge=0)    
    
class Usuario(BaseModel):
    nome_usuario: str = Field(min_length=6,max_length=20)
    nome_completo:str= Field(min_length=6, max_length=20)
    cargo: str = Field(min_length=2, max_length=20)
    
    @validator('nome_usuario')
    def validar_nome_usuario(texto:str)->str:
        return Utilidades.is_alpha_dot(texto)    

    @validator('nome_completo')
    def validar_nome_completo(texto:str)->str:
        return Utilidades.is_alpha_space(texto)
    
    @validator('cargo')
    def validar_Cargo(texto:str)->str:
        return Utilidades.is_alnum_space(texto)
    
class cadastro(BaseModel):
    nome_completo:str = Field(min_length=6,max_length=20)
    cargo:str = Field(min_length=6, max_length=20)
    senha:SecretStr = Field(min_length=6,max_length=20)   
    
    @validator('nome_completo')
    def validar_nome_completo(texto:str)->str:
        return Utilidades.is_alpha_space(texto)
    
    @validator('cargo')
    def validar_Cargo(texto:str)->str:
        return Utilidades.is_alnum_space(texto)
    
    @validator('senha')
    def validar_senha(senha:SecretStr)->SecretStr:
        return Utilidades.validar_senha(senha)
           
class BearerToken(BaseModel):
    access_token:str
    token_type: Literal['bearer'] = Field(default='bearer')    
    
    
    
    
    
    
    
    
    
    
    
        

       
        