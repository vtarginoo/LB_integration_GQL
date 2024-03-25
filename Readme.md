# Servidor Graph QL usando o Straweberry

Este projeto é um servidor usando a tecnologia do GraphQl com a biblioteca Strawberry\*\*

Objetivo: Fazer uma pesquisa personalizada na API Externa [Google Books Api](https://developers.google.com/books)

Usando o GraphQL como um intermediário entre o Front-end e a API do Google, podemos evitar o over-fetching de dados visto que a Google API retorna uma quantidade extensa de dados.

Além disso, podemos aproveitar o Cache que o GraphQL permite para que evite ultrapassar o limite de uso diário da API do Google.

As principais tecnologias que serão utilizadas aqui é o:

- [Strawbery](https://strawberry.rocks/docs)
- [Uvicorn](https://www.uvicorn.org/)
- [HTTPX](https://www.python-httpx.org/)

---

### Instalação

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---

### Executando o servidor

Para executar a API basta executar:

```
(env)$ python main.py
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ python main.py --reload
```

---

### Acesso no browser

Abra o [http://localhost:8001/graphql/](http://localhost:8001/graphql/) no navegador para verificar o status da API em execução.

---

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t gql-straberryapi .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 8001:8001 gql-straberryapi
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:8001/graphql/](http://localhost:8001/graphql/) no navegador.

### Alguns comandos úteis do Docker

> **Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
> ```
> $ docker images
> ```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>
> ```
> $ docker rmi <IMAGE ID>
> ```
>
> Subistituindo o `IMAGE ID` pelo código da imagem
>
> **Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
> ```
> $ docker container ls --all
> ```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>
> ```
> $ docker stop <CONTAINER ID>
> ```
>
> Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>
> ```
> $ docker rm <CONTAINER ID>
> ```
>
> Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).
