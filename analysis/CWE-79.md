## CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- https://cwe.mitre.org/data/definitions/79.html

---
## Descrição
Cross-site Scripting é uma vulnerabilidade que permite que um atacante execute scripts do lado do cliente, em páginas Web. Quando outros utilizadores carregam as páginas afetadas, os scripts maliciosos são executados pelo browser. Com isto, o atacante consegue aceder facilmente a cookies, tokens de sessões, entre outras informações.

Na página *Feedback* da nossa aplicação, o utilizador insere um texto, que será exibido na própria página, sem qualquer tratamento.

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


---
## Solução

Para corrigir este problema, é necessário que o texto seja tratado, antes de ser apresentado. O Flask disponibiliza um filtro ```escape```, com esse intuito, pelo que nos bastou remover o ```autoescape false``` do código, para que ele funcionasse.

**Código exemplo**:
```jinja
{% for msg in feedback %}
    <p>
        {{msg.message}}
    </p>
{% endfor %}
```

