# Criando o cliente do supabase
from supabase import create_client, Client
import os
import time

# Essas são minhas chaves de acesso ao supabase, não compartilhe com ninguém!!
# Dentro do Dashboard do Projeto, selecionar Project Settings -> API -> API Settings
# Copiar o valor de URL e colocar na variável url
url: str = "https://mbivubybidjkektfefjh.supabase.co"
# Copiar a Project API Keys. IMPORTANTE: por hora, utilizar a service_role key.
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1iaXZ1YnliaWRqa2VrdGZlZmpoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NTcyOTYwMiwiZXhwIjoyMDAxMzA1NjAyfQ.yiPBjxnpvURnzywWaxgNJM9y3jHk79jKiim3i0vFcVo"

# Cria o cliente para conectar na API do supabase
supabase: Client = create_client(url, key)

# Nome do bucket utilizado
bucket_name: str = "arquivos"

# Pega todas os arquivos do bucket
res = supabase.storage.from_(bucket_name).list()
# print(res)

# Passa por todos os arquivos de um diretório
lista_arquivos = os.listdir("./images")

# Envia os arquivos do diretório para o bucket
for arquivo in lista_arquivos:
    with open(os.path.join("./images", arquivo), 'rb+') as f:
        dados = f.read()
        res = supabase.storage.from_(bucket_name).upload(f"{time.time()}_{arquivo}", dados)
        print(res)