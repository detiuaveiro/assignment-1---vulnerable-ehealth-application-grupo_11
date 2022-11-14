# assignment-1---vulnerable-ehealth-application-grupo_11

## Grupo de desenvolvimento
- Pedro Rodrigues (102778)
- Rafael Gonçalves (102534)
- Leonardo Almeida (102536)
- Anzhelika Tosheva (103740)

## Organização do projeto
```app```: contém a aplicação insegura e um [README.md](app/README.md) com as instruções para fazer o *build* e correr a imagem Docker.

```app_sec```: contém a aplicação segura e um [README.md](app_sec/README.md) com as instruções para fazer o *build* e correr a imagem Docker.

```report```: descreve as funcionalidades do site e as suas vulnerabilidades, com o respetivo score e solução encontrada para a sua eliminação.

```analysis```: inclui evidências textuais e visuais da exploração de cada vulnerabilidade.

<br />

# Vulnerabilidades exploradas
[CWE-20: Improper Input Validation]()

[CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')]()

[CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')]()

[CWE-200: Exposure of Sensitive Information to an Unauthorized Actor]()

[CWE-256: Plaintext Storage of a Password]()

[CWE-285: Improper Authorization]()

[CWE-352: Cross-Site Request Forgery (CSRF)]()

[CWE-359: Exposure of Private Information ('Information Exposure')]()

[CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')]()

[CWE-434: Unrestricted Upload of File with Dangerous Type]()

[CWE-862: Missing Authorization]()