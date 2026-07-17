import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect("database/produtos.db")

def criar_tabela():

    conn = conectar()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (

            id TEXT PRIMARY KEY,

            titulo TEXT,

            preco REAL,
            preco_anterior REAL,
            desconto INTEGER,

            comissao TEXT,

            avaliacao REAL,
            qtd_vendidos TEXT,

            product_id TEXT,
            user_product_id TEXT,

            tipo_produto TEXT,
            extra_commission TEXT,

            imagem_id TEXT,

            url_original TEXT,

            status TEXT,
            
            data_importacao TEXT,
            
            score INTEGER,
            
            classificacao TEXT,
            
            link_afiliado TEXT,
            link_afiliado_longo TEXT
        )
    """)

    conn.commit()
    conn.close()
    
def salvar_produto(produto):

    conn = conectar()
    conn.execute("""
        INSERT OR REPLACE INTO produtos (
            id,
            titulo,
            preco,
            preco_anterior,
            desconto,
            comissao,
            avaliacao,
            qtd_vendidos,
            product_id,
            user_product_id,
            tipo_produto,
            extra_commission,
            imagem_id,
            url_original,
            status,
            data_importacao,
            score,
            classificacao,
            link_afiliado,
            link_afiliado_longo
         )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)
    """, (
        produto["id"],
        produto["titulo"],
        produto["preco"],
        produto["preco_anterior"],
        produto["desconto"],
        produto["comissao"],
        produto["avaliacao"],
        produto["qtd_vendidos"],
        produto["product_id"],
        produto["user_product_id"],
        produto["tipo_produto"],
        produto["extra_commission"],
        produto["imagem_id"],
        produto["url_original"],
        produto["status"],
        datetime.now().isoformat(),
        produto["score"],
        produto["classificacao"],
        produto["link_afiliado"],
        produto["link_afiliado_longo"]
        #produto["categoria"]
    ))

    conn.commit()
    conn.close()
    
def atualizar_status(id_produto, novo_status):

        conn = conectar()

        conn.execute("""
            UPDATE produtos
            SET status = ?
            WHERE id = ?
        """, (novo_status, id_produto))

        conn.commit()
        conn.close()
    
def buscar_por_status(status):

    conn = conectar()

    cursor = conn.execute("""
        SELECT *
        FROM produtos
        WHERE status = ?
    """, (status,))

    resultados = cursor.fetchall()

    conn.close()

    return resultados