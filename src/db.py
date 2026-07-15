import sqlite3

def conectar():
    return sqlite3.connect("database/produtos.db")

def criar_tabela():

    conn = conectar()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id TEXT PRIMARY KEY,
            titulo TEXT,
            preco REAL,
            comissao TEXT,
            url_original TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
    
def salvar_produto(produto):

    conn = conectar()
    conn.execute("""
        INSERT OR REPLACE INTO produtos (id,titulo,preco,comissao,url_original,status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        produto["id"],
        produto["titulo"],
        produto["preco"],
        produto["comissao"],
        produto["url_original"],
        produto["status"]
    ))

    conn.commit()
    conn.close()