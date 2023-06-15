# Construção de interface com Supabase

## Envio de Arquivos Simples

O arquivo fonte em questão para o primeiro envio de dados é o ***enviar_arquivo_base.py***. Nosso objetivo nesse Script, é enviar uma imagem do diretório local "images" para o Supabase.

## Leitura de Arquivos Simples

O arquivo fonte em questão é o ***ler_arquivo_base.py***. Nosso objetivo nesse Script, é ler uma imagem do Supabase para um repositório local "recebi".

# Organizando melhor o repositório

Pessoal até aqui, os dois exemplos que estavam presentes aqui eram básicos para utilização do Supabase como *File Storage*. Os proximos passos serão um pouco mais direcionados para utilizar o Supabase com a nossa aplicação.

A primeira mudança, vai ser no formato de armazenar nossas chaves de acesso. Para isso, vamos utilizar a biblioteca [***prettyconf***](https://prettyconf.readthedocs.io/en/latest/usage.html). O seu objetivo será retirar do nosso arquivo fonte, chaves de acesso. Ela vai ler essas chaves do arquivo ***keys.env***. Este arquivo ***DEVE*** estar no seu gitignore, para que essas chaves não sejam passadas também. Para efeito de estudo, vou deixar o arquivo ***keys.env.template*** no repositório. Ele contem os nomes das variáveis que serão utilizadas, mas não os seus respectivos valores.

As configurações do Supabase funcionando em conjunto com frameworks Web de Python. Cada diretório vai possuir sua própria configuração de **venv**, que estará nos arquivos de **requirements.txt** de cada diretório.

