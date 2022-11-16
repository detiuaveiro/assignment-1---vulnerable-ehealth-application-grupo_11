# eHealth Corp

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




"After reading the report, a reader should be able to understand the application, the vulnerabilities, their exploration and impact, and how they can be avoided."
