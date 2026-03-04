import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conexao = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )
    
    cursor = conexao.cursor()
    print("✅ CONECTADO AO SUPABASE COM SUCESSO!")

    cursor.execute("SELECT * FROM vendas;")
    vendas = cursor.fetchall()

    print("\n--- RELATÓRIO DE VENDAS ---")
    for venda in vendas:
        print(f"ID: {venda[0]} | Produto: {venda[3]} | Valor: R$ {venda[2]}")

    cursor.close()
    conexao.close()

except Exception as e:
    print(f"❌ Erro de conexão: {e}")
