from repositorio_cardapio import RepositorioCardapio

# CRIAR UMA VARIAVEL QUE REFERE-SE A CLASSE DO BANCO DE DADOS 
teste_cardapio = RepositorioCardapio('bd.sqlite')

# AQUI CRIAMOS UM ITEM DENTRO DO BANCO
#teste_cardapio.criar_cardapio('Feijoadas', 'Feijão Preto', 'Feijão Preto com Carnes')
#teste_cardapio.criar_cardapio('Sorvetes', 'Sorvete de Chocolate', 'Sorvete de Chocolate com Granola')
#teste_cardapio.criar_cardapio('Petiscos', 'Carne do Sol e Batata', 'Carne do Sol com Batata Frita')

teste_cardapio.atualizar_cardapios('Sorvetes', 'Sorvete de Chocolate', 'Sorvete de Chocolate com Granola')
                                   
# CRIAMOS UMA VARIAVEL PARA RETORNAR A CONSULTA EM CARDAPIO
alpha = teste_cardapio.consultar_cardapios()

# AQUI PEDIMOS PARA PRINTAR NA TELA
print(alpha)
#=======================================================================================

# AQUI NESSE CASO APAGAMOS UM ITEM DE CARDAPIOS QUE ESTÁ COM CODIGO = 'FEIJOADA'
#teste_cardapio.deletar_cardapios('Feijoadas')

# AQUI FIZEMOS UMA NOVA CONSULTA EM CARDAPIO DEPOIS DE APAGAR O ITEM 'FEIJOADA'
#alpha = teste_cardapio.consultar_cardapios()

# AQUI PEDIMOS PARA PRINTAR NA TELA  
#print(alpha)
