import sqlite3

if __name__ == '__main__':
    
    with open('criar_cardapio.sql', 'r' ) as file:
        sql_code = file.read()   
    
    # AQUI FAZEMOS A CONEXÃO
    connection = sqlite3.connect('bd.sqlite') 
    cursor = connection.cursor()
   
    cursor.executescript(sql_code)
    
   # AQUI VALIDAMOS O QUE FOI PASSADO
    connection.commit() 
    
    # AQUI NOS FECHAMOS  
    cursor.close()
    connection.close()
    
    #==================================================================
     
    # AQUI EXECUTA O CURSOR:
    # cursor.execute('SELECT * FROM produtos;')
    # AQUI ELE VAI BUSCAR TUDO 'FECHALL'
    #produtos = cursor.fetchall()
    #print(produtos)
    
    #cursor.execute("SELECT * FROM cardapio WHERE codigo = 'massas' LIMIT 1")
    # AQUI ELE VAI BUSCAR APENAS UMA LINHA 'FECHONE'
    #cardapios = cursor.fetchone()
    #print(cardapios)
    
    #cursor.execute("INSERT INTO cardapio (codigo,nome, descricao) VALUES('bebidas', 'Bebidas','alcoolica'),('frituras', 'Frituras','padrao')")
    #cursor.execute('SELECT changes();')
    #resposta = cursor.fetchone()[0]
    #print(resposta)
    
    
    