## CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- https://cwe.mitre.org/data/definitions/79.html

---
## Descrição

No *Feedback*, o utilizador insere um texto, que será exibido na própria página, sem qualquer tratamento.

**Código exemplo**:
```jinja
{% for msg in feedback %}
    <p>
        {% autoescape false %}
            {{msg.message}}
        {% endautoescape %}
    </p>
{% endfor %}
```

Deste modo, o utilizador consegue injetar HTML e até mesmo executar código JavaScript, dentro de um marcador ```<script>```.

---
## Explorar a vulnerabilidade

Para esse efeito, basta inserir um texto com código HTML na mensagem de feedback.

**Código exemplo**:
```html
<script>alert('XSS')</script>
```

# TODO -> Mostrar screenshots

Desta forma, o utilizador consegue fazer vários ataques XSS, como por exemplo:
- Ler cookies do utilizador (por exemplo, o cookie de sessão) e enviá-los para um servidor remoto
- Redirecionar o utilizador para um site malicioso
- etc.

---
## Solução

Para corrigir esse problema, é necessário que o texto seja tratado antes de ser inserido no HTML. Para isso, é possível utilizar o filtro `escape` do Flask, neste caso, como é feito automaticamente, basta remover o `autoescape false` do código.

**Código exemplo**:
```jinja
{% for msg in feedback %}
    <p>
        {{msg.message}}
    </p>
{% endfor %}
```

<br>

Desta forma, o texto será tratado antes de ser inserido no HTML, e o código HTML não será executado.

