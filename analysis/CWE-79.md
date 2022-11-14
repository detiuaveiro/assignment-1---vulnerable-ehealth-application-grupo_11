## CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- https://cwe.mitre.org/data/definitions/79.html

---
## Descrição

Na página *Feedback*, o utilizador pode inserir um texto que será exibido nesta. O texto é inserido no HTML da página, sem qualquer tratamento.

Código exemplo:
```html
{% for msg in feedback %}
    <p>
        {% autoescape false %}
            {{msg.message}}
        {% endautoescape %}
    </p>
{% endfor %}
```

Isso permite que o utilizador insira código HTML, que será executado pelo navegador.

---
## Explorar a vulnerabilidade

Para explorar a vulnerabilidade, basta inserir um texto com código HTML na mensagem de feedback.

Código exemplo:
```html
<script>alert('XSS')</script>
```

# TODO -> Mostrar screenshots

Desta forma, o utilizador consegue fazer vários ataques XSS, como por exemplo:
- Ler cookies do utilizador (por exemplo, o cookie de sessão) e enviá-los para um servidor remoto

---
## Solução

Para corrigir esse problema, é necessário que o texto seja tratado antes de ser inserido no HTML. Para isso, é possível utilizar o filtro `escape` do Flask, neste caso, como é feito automaticamente, basta remover o `autoescape false` do código.

Código exemplo:
```html
{% for msg in feedback %}
    <p>
        {{msg.message}}
    </p>
{% endfor %}
```

<br>

Desta forma, o texto será tratado antes de ser inserido no HTML, e o código HTML não será executado.

