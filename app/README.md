# Execução da aplicação insegura

Dentro da pasta ```app```, execute os seguintes comandos no terminal:
### *Build* da imagem Docker com a aplicação

```docker build -t [NOME_IMAGEM] .```

Exemplo:

```docker build -t app .```

### Execução da imagem Docker com a aplicação

```docker run --name [NOME_CONTAINER] -p [PORTA]:8001 [NOME_IMAGEM]:latest```

Exemplo:

```docker run --name app_container -p 8001:8001 app:latest```

### Acesso à aplicação
A aplicação web estará disponível em http://localhost:[PORTA].

</br>

>**Nota**: Os campos NOME_IMAGEM, NOME_CONTAINER e PORTA são arbitrários, devendo apenas ser iguais nos dois comandos.
