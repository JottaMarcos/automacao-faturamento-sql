import psycopg2
import os

try:
    # Colocando os dados DIRETO aqui para o GitHub não ter como errar
    conexao = psycopg2.connect(
        host="aws-0-sa-east-1.pooler.supabase.com",
        user="postgres.ltaxntxapuekaguwuylj",
        password="Jottamarcos07", # <--- COLOQUE A SENHA QUE VOCÊ CRIOU
        database="postgres",
        port="6543"
    )
    
    cursor = conexao.cursor()
    print("✅ CONEXÃO ESTABELECIDA COM O SUPABASE!")

    cursor.execute("SELECT * FROM vendas;")
    vendas = cursor.fetchall()

    for venda in vendas:
        print(f"Produto: {venda[3]} | Valor: R$ {venda[2]}")

    cursor.close()
    conexao.close()

except Exception as e:
    print(f"❌ Erro real de conexão: {e}")
