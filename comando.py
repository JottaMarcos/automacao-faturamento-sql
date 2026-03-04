import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis (do .env local ou dos Secrets do GitHub)
load_dotenv()

try:
    # Conecta ao Supabase usando as novas chaves
    conexao = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )
    
    cursor = conexao.cursor()
    print("✅ Conectado ao Supabase com sucesso!")

    # Busca os dados que você inseriu via SQL
    cursor.execute("SELECT * FROM vendas;")
    vendas = cursor.fetchall()

    print("\n--- RELATÓRIO DE VENDAS NA NUVEM ---")
    for venda in vendas:
        print(f"ID: {venda[0]} | Produto: {venda[3]} | Valor: R$ {venda[2]}")

    cursor.close()
    conexao.close()

except Exception as e:
    print(f"❌ Erro ao conectar: {e}")
