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
        {{ msg.message | safe }}
    </p>
{% endfor %}
```

Deste modo, o utilizador consegue injetar HTML e até mesmo executar código JavaScript, dentro de um marcador ```<script>```.

---
## Explorar a vulnerabilidade

Para esse efeito, basta inserir um excerto de HTML, na mensagem de feedback.

**Código exemplo**:
```html
<script>
    alert(document.cookie);
</script>
```
>*Nota*: Em client-side scripts, não é possível aceder a cookies com a flag ```HTTPOnly```. Porém, se essa flag tiver valor 'false', o cookie é exibido, usando o código acima. Abordamos este tópico na vulnerabilidade [CWE-1004](CWE-1004.md).

# TODO -> Mostrar screenshots

---
## Solução

Para corrigir este problema, é necessário que o texto seja tratado, antes de ser apresentado. Nesse sentido, o Jinja (mecanismo de templating que o Flask usa) ativa o *autoescaping*, por defeito, para todas as páginas HTML renderizadas com o método ```render_template()```, algo que é imcompatível com o filtro ```safe```, que identifica um excerto dinâmico de HTML como seguro.

**Código exemplo**:
```jinja
{% for msg in feedback %}
    <p>
        {{ msg.message }}
    </p>
{% endfor %}
```

