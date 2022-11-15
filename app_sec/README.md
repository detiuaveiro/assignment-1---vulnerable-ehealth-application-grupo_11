# Execução da aplicação segura

Dentro da pasta ```app_sec```, execute os seguintes comandos no terminal:
## *Build* da imagem Docker com a aplicação

```docker build -t [NOME] .```

## Execução da imagem Docker com a aplicação
De seguida, execute o seguinte comando:

```docker run -p [PORTA]:[PORTA] [NOME]```

</br>

>**Nota**: Os campos NOME e PORTA são arbitrários, devendo apenas ser iguais nos dois comandos. Não obstante, o NOME não deve colidir com aquele que foi utilizado para a aplicação insegura.