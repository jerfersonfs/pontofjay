import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect("database/produtos.db")

def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()
    
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
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id TEXT NOT NULL,
            queue TEXT NOT NULL,
            status TEXT DEFAULT 'PENDENTE',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(product_id, queue),

            FOREIGN KEY (product_id)
                REFERENCES produtos(id)
        )
    """)

    conn.commit()
    conn.close()
    
def salvar_produto(produto):
    
    try:
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
    except Exception as erro:
        print(f"Erro ao salvar produto no database:{erro}")
    finally:
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

def produto_existe(id_produto):

    conn = conectar()

    cursor = conn.execute("""
        SELECT 1
        FROM produtos
        WHERE id = ?
        LIMIT 1
    """, (id_produto,))

    existe = cursor.fetchone() is not None

    conn.close()

    return existe

def adicionar_a_fila(product_id, queue):

    conn = conectar()

    try:
        conn.execute("""
            INSERT OR IGNORE INTO product_queue (
                product_id,
                queue
            )
            VALUES (?, ?)
        """, (product_id, queue))

        conn.commit()

    finally:
        conn.close()