from fastapi import APIRouter, HTTPException, status, Depends
#import db # 'AQUI IMPORTAVA QUANDO ERA O BANCO FALSO'
import dtos
from util import Utilidades
from dependencias import obter_repo_cardapio, obter_repo_produto
from repositorio_produto import RepositorioProduto
from repositorio_cardapio import RepositorioCardapio

router = APIRouter()

@router.get('/produto/')
async def listar_produtos(codigo_cardapio: str = ' ', 
   preco_min: int = -1, preco_max: int = 9999, restricao: str =' ',
   repo_cardapio:RepositorioCardapio = Depends(obter_repo_cardapio),
   repo_produto:RepositorioProduto = Depends(obter_repo_produto)):
    
   if codigo_cardapio != ' ' and not repo_cardapio.consultar_cardapios(codigo_cardapio):
      raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'CARDAPIO NOT FOUND') 
    #for produtos in db.produtos.values():    
    #        if (produtos['valor'] >= preco_min and produtos['valor'] <= preco_max
    #            and(restricao == ' ' or produtos['restricao'] == restricao)
    #            and(codigo_cardapio == ' ' or produtos['codigo_cardapio'] == codigo_cardapio)):

    #             listados.append(produtos)
    
   listados = repo_produto.consultar_produto(preco_min, preco_max, codigo_cardapio, restricao) 
    
   return listados

@router.get('/produto/{codigo_produto}')
async def consultar_produto(codigo_produto: str, 
   repo_produto:RepositorioProduto = Depends(obter_repo_produto)):    
    
   encontrado = repo_produto.consultar_produto(consultar_produto) 
    
   if not encontrado:
       raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'PRODUTO NOT FOUND')
    
   return encontrado

@router.post('/produto/', status_code= status.HTTP_201_CREATED)
async def cadastrar_produto(produto: dtos.ProdutoIn, util: Utilidades = Depends(Utilidades),
   repo_cardapio:RepositorioCardapio = Depends(obter_repo_cardapio),
   repo_produto:RepositorioProduto = Depends(obter_repo_produto)):    
    
   cardapio = repo_cardapio.consultar_cardapios(produto.codigo_cardapio)
   
   if not cardapio: 
       raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'CARDAPIO NOT FOUND')
    
   codigo = util.criar_codigo(produto.nome)
    
   encontrado = repo_produto.consultar_produto(codigo)
    
   if not encontrado: 
       raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= 'PRODUTO COM CODIGO JÁ EXISTENTE')
     
   #db.produtos[codigo] = produto.model_dump()
   #db.produtos[codigo]['codigo'] = codigo
   
   repo_produto.criar_produto(codigo, produto.nome, produto.descricao,
   produto.valor, produto.restricao, produto.codigo_cardapio)
   
   return repo_produto.consultar_produto(codigo)

@router.put('/produto/{codigo_produto}')
async def alterar_produto(codigo_produto:str, produto:dtos.ProdutoIn,
   repo_cardapio:RepositorioCardapio = Depends(obter_repo_cardapio),
   repo_produto:RepositorioProduto = Depends(obter_repo_produto)):      
   
   encontrado = repo_produto.consultar_elemento_produto(codigo_produto)
      
   if not encontrado:
      raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'PRODUTO NOT FOUND') 
   
   cardapio = repo_cardapio.consultar_elemento_cardapios(produto.codigo_cardapio)
      
   if not cardapio:
      raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'CARDAPIO NOT FOUND')
      
   #db.produtos[codigo_produto] = produto.model_dump()
   #db.produtos[codigo_produto]['codigo'] = codigo_produto
   
   repo_produto.atualizar_produto(codigo_produto, produto.nome, produto.descricao, 
   produto.codigo_cardapio, produto.valor, produto.restricao)
   
   return repo_produto.consultar_produto(codigo_produto)

@router.delete('/produto/{codigo_produto}')
async def remover_produto(codigo_produto: str,
   repo_produto:RepositorioProduto = Depends(obter_repo_produto)):    
   
   encontrado = repo_produto.consultar_produto(codigo_produto)
    
   if not encontrado:
       raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'PRODUTO NOT FOUND')
    
   return encontrado

@router.patch('/produto/{codigo_produto}') 
async def alterar_valor_produto(codigo_produto:str, valor:dtos.PrecoProduto, 
   repo_produto:RepositorioProduto = Depends(obter_repo_produto)):    
   
   encontrado = repo_produto.consultar_produto(codigo_produto) 
    
   if not encontrado:
       raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'PRODUTO NOT FOUND')
   
   repo_produto.atualizar_produto(codigo_produto, encontrado.nome, encontrado.descricao, 
   encontrado.codigo_cardapio, encontrado.valor, encontrado.restricao)
    
   #db.produtos[codigo_produto]['valor'] = valor.valor
   return repo_produto.consultar_produto(codigo_produto)    