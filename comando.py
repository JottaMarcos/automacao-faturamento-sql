import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conexao = psycopg2.connect(
        host="aws-0-sa-east-1.pooler.supabase.com",
        user="postgres.ltaxntxapuekaguwuylj",
        password=os.getenv('DB_PASS'), # Usando o Secret por segurança
        database="postgres",
        port="6543" # <-- A CHAVE ESTÁ AQUI
    )
    
    cursor = conexao.cursor()
    print("✅ CONEXÃO ESTABELECIDA!")

    cursor.execute("SELECT * FROM vendas;")
    vendas = cursor.fetchall()

    for venda in vendas:
        print(f"Produto: {venda[3]} | Valor: R$ {venda[2]}")

    cursor.close()
    conexao.close()

except Exception as e:
    print(f"❌ Erro de conexão: {e}")
