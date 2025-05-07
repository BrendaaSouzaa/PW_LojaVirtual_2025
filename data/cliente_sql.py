CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS cliente (
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Nome TEXT NOT NULL,
CPF TEXT NOT NULL,
Email TEXT NOT NULL,
Telefone TEXT NOT NULL,
Senha TEXT NOT NULL)
"""
INSERIR_CLIENTE = """
INSERT INTO cliente (Id, Nome, CPF, Email, Telefone, Senha)
VALUES (?, ?, ?, ?, ?, ?)
"""
OBTER_TODOS = """
SELECT 
Id, Nome, CPF, Email, Telefone, Senha
FROM cliente
"""