# Construção de interface com Supabase

## Envio de Arquivos Simples

O arquivo fonte em questão para o primeiro envio de dados é o ***enviar_arquivo_base.py***. Nosso objetivo nesse Script, é enviar uma imagem do diretório local "images" para o Supabase.

## Leitura de Arquivos Simples

O arquivo fonte em questão é o ***ler_arquivo_base.py***. Nosso objetivo nesse Script, é ler uma imagem do Supabase para um repositório local "recebi".

# Organizando melhor o repositório

Pessoal até aqui, os dois exemplos que estavam presentes aqui eram básicos para utilização do Supabase como *File Storage*. Os proximos passos serão um pouco mais direcionados para utilizar o Supabase com a nossa aplicação.

A primeira mudança, vai ser no formato de armazenar nossas chaves de acesso. Para isso, vamos utilizar a biblioteca [***prettyconf***](https://prettyconf.readthedocs.io/en/latest/usage.html). O seu objetivo será retirar do nosso arquivo fonte, chaves de acesso. Ela vai ler essas chaves do arquivo ***keys.env***. Este arquivo ***DEVE*** estar no seu gitignore, para que essas chaves não sejam passadas também. Para efeito de estudo, vou deixar o arquivo ***keys.env.template*** no repositório. Ele contem os nomes das variáveis que serão utilizadas, mas não os seus respectivos valores.

As configurações do Supabase funcionando em conjunto com frameworks Web de Python. Cada diretório vai possuir sua própria configuração de **venv**, que estará nos arquivos de **requirements.txt** de cada diretório.

## Integração com FastAPI

Dentro do diretório: ***integracao-fastapi***.

Todo o código-fonte está dentro do diretório **/src**. Apenas um README foi criado para o projeto para facilitar a localização das informações. O objetivo deste projeto é integrar o FastAPI com o Supabase. Possibilitando as seguintes funcionalidades:
- Receber um POST com uma imagem e subir ela no Supabase. Se nenhum ID de projeto vier associado a imagem que foi enviada, este projeto será carregado na coleção "anonymous".
- Receber um GET para conhecer todas as coleções que estão cadastradas.
- Receber um GET para conhecer todas as imagens cadastradas em uma determinada coleção.
- Receber um GET para buscar as informações de uma imagem específica de uma coleção.
- Receber um PUT para atualizar uma imagem em uma coleção.
- Receber um DELETE para apagar uma imagem em uma coleção.
- Receber um DELETE para apagar uma coleção.
- Uma página estática mínima para demonstrar as funcionalidades implementadas.

A configuração da aplicação com [FastAPI](https://fastapi.tiangolo.com/) já preve a utilização do framework estruturando os recursos do projeto. A estrutura da solução será:
```sh
./src
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── image.py
│   │   └── collection.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── image.py
│   │   └── collection.py
│   └── services
│       ├── __init__.py
│       ├── image.py
│       └── collection.py
├── static
│   └── index.html
./keys.env
./requirements.txt
```

Cada um dos diretórios tem uma funcionalidade:
- ***app***: Este diretório contém todo o código da sua aplicação.
- ***main.py***: Este é o ponto de entrada da sua aplicação. Aqui você vai criar a instância do FastAPI e incluir todas as rotas.
- ***models***: Este diretório contém todos os modelos de dados que a sua aplicação irá usar.
- ***routes***: Este diretório contém todos os arquivos de rotas da sua aplicação. Cada arquivo define as rotas para um recurso específico.
- ***services***: Este diretório contém todo o código que implementa a lógica de negócio da sua aplicação. Cada arquivo implementa as operações para um recurso específico.
- ***static***: Este diretório contém todos os arquivos estáticos da sua aplicação.

O [***Pydantic***](https://docs.pydantic.dev/latest/) serve para validar os dados recebidos em uma requisição. Com ele, modelamos um classe que deve conter os campos necessários em um POST que será realizado. Dsta forma, se o POST não vier com as informações necessárias, o FastAPI já devolve um erro para quem fez a requisição. Além disso, esses comportamento são monitorados pela API do Swagger para realizar a documentação de forma automática.