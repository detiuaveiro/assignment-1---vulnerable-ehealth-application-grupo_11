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

<br/>

# Vulnerabilidades exploradas
[CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')](analysis/CWE-79.md)

[CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')](analysis/CWE-89.md)

[CWE-209: Generation of Error Message Containing Sensitive Information](analysis/CWE-209.md)

[CWE-257: Storing Passwords in a Recoverable Format](analysis/CWE-257.md)

[CWE-352: Cross-Site Request Forgery (CSRF)](analysis/CWE-352.md)

[CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')](analysis/CWE-400.md)

[CWE-434: Unrestricted Upload of File with Dangerous Type](analysis/CWE-434.md)

[CWE-521: Weak Password Requirements](analysis/CWE-521.md)

[CWE-620: Unverified Password Change](analysis/CWE-620.md)

[CWE-862: Missing Authorization](analysis/CWE-862.md)

[CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag](analysis/CWE-1004.md)

>*Obs*: Cada link remete para a análise de uma vulnerabilidade. A descrição, o score e a solução encontrada para cada uma delas encontram-se no [relatório](report.md).
