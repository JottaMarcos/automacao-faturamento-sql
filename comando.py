import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# 1. Definimos o caminho exato do arquivo (ajustado para o seu PC)
caminho_env = r'C:\Users\João Marcos\Downloads\GIT ACTIONS\.env'

# 2. Carregamos o arquivo APENAS UMA VEZ apontando para o caminho certo
if os.path.exists(caminho_env):
    load_dotenv(dotenv_path=caminho_env)
    print(f"✅ Arquivo .env encontrado em: {caminho_env}")
else:
    print(f"❌ ERRO: O arquivo não foi encontrado no caminho: {caminho_env}")

# 3. TESTE DE VARIÁVEIS (Para termos certeza absoluta antes de conectar)
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")

print("--- DIAGNÓSTICO DE CREDENCIAIS ---")
print(f"Usuário: {user}")
print(f"Senha: {'***' if password else 'None'}") # Esconde a senha por segurança, mas avisa se existe
print(f"Banco: {database}")
print("----------------------------------")

# 4. Tenta a conexão apenas se as variáveis não forem None
if None in [user, password, host, database]:
    print("⚠️ Erro: Uma ou mais variáveis do .env não foram carregadas. Verifique o nome do arquivo!")
else:
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        print("✅ Conexão segura estabelecida com sucesso!")

        # Busca os dados
        df = pd.read_sql("SELECT * FROM vendas", conexao)
        
        print("\n--- Primeiras 5 linhas da tabela ---")
        print(df.head())

        conexao.close()

    except Exception as e:
        print(f"❌ Erro ao conectar ao MySQL: {e}")