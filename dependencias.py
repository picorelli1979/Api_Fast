from dotenv import dotenv_values
from fastapi.security import OAuth2PasswordBearer
from repositorio_cardapio import RepositorioCardapio
from repositorio_produto import RepositorioProduto
from repositorio_usuario import RepositorioUsuario
from autenticacao import Autenticador

ENV = dotenv_values()

def obter_repo_cardapio():
    return RepositorioCardapio(ENV['NOME_DB'])

def obter_repo_produto():
    return RepositorioProduto(ENV['NOME_DB'])

def obter_repo_usuario():
    return RepositorioUsuario(ENV['NOME_DB'])

def obter_autenticador():
    return Autenticador(ENV["ALGORITMO"],ENV["CHAVE_PRIVADA"],ENV["CHAVE_PUBLICA"], 
                        int(ENV["VALIDADE_TOKEN"]),int(ENV["CUSTO_SALT"]))

dependencia_token = OAuth2PasswordBearer(tokenUrl=ENV["URL_TOKEN"])    