# eHealth Corp

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Aplicação Insegura](#aplicação-insegura)
3. [Analise de Vulnerabilidades](#análise-de-vulnerabilidades)
    - [CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')](#cwe-79-improper-neutralization-of-input-during-web-page-generation-cross-site-scripting)
    - [CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')](#cwe-89-improper-neutralization-of-special-elements-used-in-an-sql-command-sql-injection)
    - [CWE-209: Generation of Error Message Containing Sensitive Information](#cwe-209-generation-of-error-message-containing-sensitive-information)
    - [CWE-257: Storing Passwords in a Recoverable Format](#cwe-257-storing-passwords-in-a-recoverable-format)
    - [CWE-352: Cross-Site Request Forgery (CSRF)](#cwe-352-cross-site-request-forgery-csrf)
    - [CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')](#cwe-400-uncontrolled-resource-consumption-resource-exhaustion)
    - [CWE-434: Unrestricted Upload of File with Dangerous Type](#cwe-434-unrestricted-upload-of-file-with-dangerous-type)
    - [CWE-521: Weak Password Requirements](#cwe-521-weak-password-requirements)
    - [CWE-620: Unverified Password Change](#cwe-620-unverified-password-change)
    - [CWE-862: Missing Authorization](#cwe-862-missing-authorization)
4. [Conclusão](#conclusão)

---

## Descrição do Projeto
eHealth Corp é uma aplicação web de uma clínica, que oferece aos seus utilizadores serviços médicos de diferentes especialidades.

A aplicação tem como alvo final as seguintes entidades:
1. Paciente
2. Médico

Através da aplicação, tanto médicos como pacientes podem:
- Registar-se
- Iniciar e encerrar sessão
- Alterar definições de conta (alterar password)
- Aceder à lista de todos os médicos registados na plataforma, bem como todas as suas informações
- Dar opinião/feedback relativamente ao serviço
- Aceder à lista de serviços oferecidos
- Aceder aos contactos da clínica


Para além das funcionalidades supracitadas, os pacientes podem ainda:
- Marcar consultas
- Ver todas as consultas marcadas
- Fazer Download de resultados de testes disponibilizados previamente por um médico


Enquanto médico, é também possível:
- Aceder à lista de consultas marcadas pelos pacientes
- Submeter resultados dos testes dos pacientes

Para fins educacionais foram desenvolvidas duas versões da aplicação, uma versão insegura e uma versão segura.

<br />

## Aplicação insegura

Como dito anteriormente, foi desenvolvida uma versão insegura da aplicação (<code>app</code>). Esta versão apresenta diferentes tipos de vulnerabilidades, vulnerabilidades essas que podem ser exploradas e por sua vez comprometer a segurança, integridade e usabilidade do sistema.

Ao longo deste relatório, para cada vulnerabilidade da aplicação iremos apresentar uma breve descrição, justificar o score atribuído, como pode ser explorada, o impacto associado e por fim uma possível solução.

As vulnerabilidades presentes na versão insegura são as seguintes:

- CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- CWE-209: Generation of Error Message Containing Sensitive Information
- CWE-257: Storing Passwords in a Recoverable Format
- CWE-352: Cross-Site Request Forgery (CSRF)
- CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')
- CWE-434: Unrestricted Upload of File with Dangerous Type
- CWE-521: Weak Password Requirements
- CWE-620: Unverified Password Change
- CWE-862: Missing Authorization

<br />

## Análise de vulnerabilidades

### CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

#### Descrição
Cross-site Scripting é uma vulnerabilidade de segurança que permite que um atacante execute scripts do lado do cliente (geralmente JavaScript) em páginas da Web. Quando outros utilizadores carregarem as páginas afetadas, os scripts maliciosos serão executados, permitindo que o atacante obtenha cookietokens de sessões ou outras informações.

#### Exploração
Na página *Feedback* da aplicação, qualquer utilizador logged in pode publicar uma mensagem de feedback relativamente ao serviço. 

A exploração desta vulnerabilidade passa por publicar uma mensagem que contenha um script. Sempre que as mensagens de feedback forem apresentadas, este script será executado pelo browser do utilizador.

Uma exploração concreta desta vulnerabilidade pode ser encontrada na pasta <code>analysis</code>.

#### Impacto
O impacto associado a esta vulnerabilidade varia consoante a complexidade do código do atacante que é executado pelo browser do utilizador.


#### Score
Attack Vector (AV):
Attack Complexity (AC):
Privileges Required (PR):
User Interaction (UI):
Scope (S):
Confidentiality (C):
Integrity (I):
Availability (A):
Final Base Score:

#### Solução
O jinja2 por default já faz isso? Meto essa shit?????

### CWE-89: SQL Injection
#### Descrição
SQL Injection é um outro tipo de vulnerabilidade onde o atacante por meio de formulários ou outros campos que envolvem acesso à base de dados, introduzem código SQL que neutraliza certos comandos presentes na query. Estes comandos neutralizados podem ser fundamentais para a segurança do sistema, como por exemplo no processo de autenticação.


#### Exploração
Na aplicação insegura existem certas páginas onde esta vulnerabilidade está presente, nomeadamente na página de **Login**, **Register** e **Doctors**.


#### Score
Attack Vector (AV):
Attack Complexity (AC):
Privileges Required (PR):
User Interaction (UI):
Scope (S):
Confidentiality (C):
Integrity (I):
Availability (A):
Final Base Score:

#### Solução

### CWE-209: Generation of Error Message Containing Sensitive Information
TODO

### CWE-257: Storing Passwords in a Recoverable Format
TODO

### CWE-352: Cross-Site Request Forgery (CSRF)
TODO

### CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')
TODO

### CWE-434: Unrestricted Upload of File with Dangerous Type
TODO

### CWE-521: Weak Password Requirements
TODO

### CWE-620: Unverified Password Change
TODO

### CWE-862: Missing Authorization
TODO



"After reading the report, a reader should be able to understand the application, the vulnerabilities, their exploration and impact, and how they can be avoided."
