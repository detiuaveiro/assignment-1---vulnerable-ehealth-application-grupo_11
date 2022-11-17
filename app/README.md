# Execução da aplicação insegura

Dentro da pasta ```app```, execute os seguintes comandos no terminal:
## *Build* da imagem Docker com a aplicação

```docker build -t [NOME_IMAGEM] .```

## Execução da imagem Docker com a aplicação
De seguida, execute o seguinte comando:

```docker run --name [NOME_CONTAINER] -p 8001:[PORTA] [NOME_IMAGEM]:latest```

## Acesso à aplicação
A aplicação web estará disponível em http://localhost:[PORTA].

</br>

>**Nota**: Os campos NOME_IMAGEM, NOME_CONTAINER e PORTA são arbitrários, devendo apenas ser iguais nos dois comandos.