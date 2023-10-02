PRAGMA foreign_keys=ON;

BEGIN TRANSACTION ;

CREATE TABLE IF NOT EXISTS cardapios(
   codigo TEXT PRIMARY KEY, 
   nome TEXT NOT NULL UNIQUE,
   descricao TEXT NOT NULL  
);
INSERT INTO cardapios (codigo, nome, descricao) 
VALUES
('massas', 'Massas', 'Massas da casa'),
('sobremesas', 'Sobremesas', 'Sobremesas da casa'),
('fastfood', 'Fast Food', 'Comidas rápidas da casa');  

CREATE TABLE IF NOT EXISTS produtos(

    codigo TEXT PRIMARY KEY,  
    nome TEXT NOT NULL UNIQUE, 
    descricao TEXT NOT NULL,
    preco REAL NOT NULL, 
    restricao TEXT NOT NULL,
    codigo_cardapio TEXT NOT NULL,
    
    FOREIGN KEY (codigo_cardapio) REFERENCES cardapios(codigo)
    ON UPDATE RESTRICT ON DELETE RESTRICT

);

INSERT INTO produtos (codigo, nome, descricao, preco, restricao, codigo_cardapio) 
VALUES
('penne', 'Penne', 'Penne ao molho', 19.90, 'vegeteriano','massas' ),
('talharim', 'Talharim', 'Talharim ao molho', 19.90, 'vegeteriano','massas' ),
('petit-gateau', 'Petit Gateau', 'Petit Gateau', 9.90, 'vegeteriano','sobremesas' );
  
CREATE TABLE IF NOT EXISTS usuario (
    nome_usuario TEXT PRIMARY KEY,
    nome_completo TEXT NOT NULL UNIQUE,
    cargo TEXT NOT NULL,
    salt_senha BLOB NOT NULL,
    hash_senha BLOB NOT NULL
);


COMMIT;  