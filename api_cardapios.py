from fastapi import APIRouter, HTTPException, status, Depends
# import db # 'NESSE CASO AQUI O BANCO FALSO NÃO USA MAIS  '
import dtos
from util import Utilidades
from dependencias import obter_repo_cardapio,obter_repo_produto 
from repositorio_cardapio import RepositorioCardapio
from repositorio_produto import RepositorioProduto

router = APIRouter()

@router.get('/cardapio/')
async def listar_cardapios(rep_cardapio:RepositorioCardapio=Depends(obter_repo_cardapio)):
    
    return rep_cardapio.consultar_cardapios()

@router.get('/cardapio/{codigo_cardapio}')
async def consultar_cardapio(codigo_cardapio:str,
    rep_cardapio:RepositorioCardapio=Depends(obter_repo_cardapio)):    
    
    consultar = rep_cardapio.consultar_elemento_cardapios(codigo_cardapio)
    
    if not consultar:
         raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'CARDAPIO NOT FOUND')
    
    return consultar 
     
@router.post('/cardapio/', status_code=status.HTTP_201_CREATED) 
async def cadastrar_cardapio(cardapio: dtos.CardapioIn, util: Utilidades = Depends(Utilidades), 
    rep_cardapio:RepositorioCardapio=Depends(obter_repo_cardapio)):
    
    codigo = util.criar_codigo(cardapio.nome)
    
    consultar = rep_cardapio.consultar_elemento_cardapios(codigo)
    
    if consultar:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= 'CODIGO JÁ EXISTE')
    
    #db.cardapios[codigo] = cardapio.model_dump() 'AQUI QUANDO ERA BANCO FALSO
    #db.cardapios[codigo]['codigo'] = codigo  'AQUI ERA BANCO FALSO'
    
    rep_cardapio.criar_cardapio(codigo, cardapio.nome, cardapio.descricao)
    
    return rep_cardapio.consultar_elemento_cardapio()

@router.put('/cardapio/{codigo_cardapio}')
async def alterar_cardapio(codigo_cardapio:str, cardapio:dtos.CardapioIn, 
    rep_cardapio:RepositorioCardapio=Depends(obter_repo_cardapio)):    
     
    consultar = rep_cardapio.consultar_elemento_cardapios(codigo_cardapio)
    
    if consultar:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'CARDAPIO NOR FOUND')
     
     #db.cardapios[codigo_cardapio] = codigo_cardapio.model_dump() 'AQUI QUANDO ERA BANCO FALSO'
     #db.cardapios[codigo_cardapio]['codigo_cardapio'] = codigo_cardapio 'AQUI QUANDO ERA BANCO FALSO'
     
    rep_cardapio.atualizar_cardapios(codigo_cardapio,cardapio.nome,cardapio.descricao )
     
    return rep_cardapio.consultar_elemento_cardapios()
   
@router.delete('/cardapio/{codigo_cardapio}')
async def remover_cardapio(codigo_cardapio: str, 
    rep_cardapio:RepositorioCardapio=Depends(obter_repo_cardapio),
    rep_produto:RepositorioProduto=Depends(obter_repo_produto)):   
    
    consultar = rep_cardapio.consultar_elemento_cardapios(codigo_cardapio)
    
    if not consultar:
       raise HTTPException(status.HTTP_404_NOT_FOUND,detail= 'CARDAPIO NOT FOUND')
   
    if rep_produto.consultar_produto(codigo_cardapio=codigo_cardapio): 
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= 'NÃO É POSSIVEL DELETAR, CARDAPIO POSSUI PRODUTOS')
    
    rep_cardapio.deletar_cardapios(codigo_cardapio)
    
    return consultar

@router.patch('/cardapio/{codigo_cardapio}')
async def alterar_descricao_cardapio(codigo_cardapio:str, 
    descricao: dtos.DescricaoCardapio,
    rep_cardapio:RepositorioCardapio=Depends(obter_repo_cardapio)):                                   
      
    consultar = rep_cardapio.consultar_elemento_cardapios(codigo_cardapio)  
      
    if not consultar:
       raise HTTPException(status.HTTP_404_NOT_FOUND, detail= 'CARDAPIO NOT FOUND')
      
    rep_cardapio.atualizar_cardapios(codigo_cardapio,descricao) 
      
    return consultar