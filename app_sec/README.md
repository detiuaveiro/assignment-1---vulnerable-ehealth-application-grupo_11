# Execução da aplicação segura

Dentro da pasta ```app_sec```, execute os seguintes comandos no terminal:
### *Build* da imagem Docker com a aplicação

```docker build -t [NOME_IMAGEM] .```

Exemplo

```docker build -t app_sec .```

>**Nota**: O passo 8/10 (RUN python3 populate.py) pode demorar, já que é feito o *hashing* das passwords dos utilizadores, antes da sua inserção na base de dados.

### Execução da imagem Docker com a aplicação

```docker run --name [NOME_CONTAINER] -p [PORTA]:8002 [NOME_IMAGEM]:latest```

Exemplo

```docker run --name app_sec_container -p 8002:8002 app_sec:latest```

### Acesso à aplicação
A aplicação web estará disponível em http://localhost:[PORTA].

</br>

>**Nota**: Os campos NOME_IMAGEM, NOME_CONTAINER e PORTA são arbitrários, devendo apenas ser iguais nos dois comandos. Não obstante, o NOME_IMAGEM e o NOME_CONTAINER não devem colidir com aqueles que foram utilizados para a aplicação insegura.
