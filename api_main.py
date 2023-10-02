from fastapi import FastAPI
import api_cardapios 
import api_produtos
import api_autenticacao

matrix = FastAPI()

matrix.include_router(api_cardapios.router)
matrix.include_router(api_produtos.router)
matrix.include_router(api_autenticacao.router)