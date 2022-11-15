## CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- https://cwe.mitre.org/data/definitions/89.html

---
## Descrição

O utilizador pode preencher campos de *input* no website com texto que será utilizado na query SQL, sem qualquer tratamento. 

Esta vulnerabilidade está presente em 3 páginas do website:
- Login
- Register
- Doctors

**Código exemplo**:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
# login
user = cur.execute(
    f"SELECT * FROM app_user \
        WHERE ( email = '{email}' ) AND ( password_ = '{password}')"
    ).fetchone()
# register
cur.executescript(
    f"INSERT INTO app_user (email, password_, name_) \
        VALUES ('{email}', '{password}', '{full_name}');"
)
# doctors
doctors = cur.execute(
    f"SELECT app_user.name_, app_user.email, doctor.speciality \
        FROM (doctor JOIN app_user ON doctor.id = app_user.id) \
        WHERE app_user.name_ LIKE '%{user_input}%'"
).fetchall()
```

Isso permite que o utilizador insira código SQL, que será executado pelo servidor.

---
## Explorar a vulnerabilidade

### Login

O utilizador consegue entrar com um email existente e uma password errada, se inserir na password:
```sql
' or 1=1 ) -- //
```

# TODO -> Mostrar screenshots

Também consegue entrar com o primeiro utilizador da base de dados, se inserir na password:
```sql
') or 1=1 -- //
```

Neste caso, o primeiro utilizador da base de dados é o admin e tem acesso a uma página que permite controlar a base de dados.

# TODO -> Mostrar screenshots

Desta forma, o utilizador consegue aceder a uma conta de outro utilizador, ou gerir a base de dados.

<br>

### Register

Nesta página, o utilizador consegue executar multiplas queries SQL, por exemplo, se inserir no nome:
```sql
'); DROP TABLE app_user; -- //
```

# TODO -> Mostrar screenshots

Desta forma utilizador pode executar qualquer query SQL na base de dados.

<br>

### Doctors

O utilizador pode executar uma query SQL de cada vez ao inseri-la no campo de pesquisa.

Por exemplo, para obter todas as tabelas e colunas da base de dados:
```sql
1' AND 1=2 UNION SELECT sql,1,1 FROM sqlite_master WHERE type='table' -- //
```

# TODO -> Mostrar screenshots

Para obter os nomes, emails e passwords de todos os utilizadores:
```sql
1' AND 1=2 UNION SELECT name_, email, password_ FROM app_user -- //
```

# TODO -> Mostrar screenshots

Desta forma, o utilizador consegue aceder a qualquer informação da base de dados.

---
## Solução

Para evitar esta vulnerabilidade, é necessário tratar o input do utilizador, para que não seja possível executar queries SQL.

O flask permite fazer esse tratamento se inserirmos as variaveis com os métodos dados.

Também devemos mudar o método de execução no *register* para executar apenas uma query.

**Código exemplo**:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
# login
user = cur.execute(
    "SELECT * FROM app_user \
        WHERE ( email = ? ) AND ( password_ = ? )", (email, password)
    ).fetchone()
# register
cur.execute(
    "INSERT INTO app_user (email, password_, name_) \
        VALUES (? ,?, ?);", (email, password, full_name)
)
# doctors
doctors = cur.execute(
    "SELECT app_user.name_, app_user.email, doctor.speciality \
        FROM (doctor JOIN app_user ON doctor.id = app_user.id) \
        WHERE app_user.name_ LIKE ?" , ('%' + user_input + '%')
).fetchall()
```

Assim, é feito o tratamento do input do utilizador, evitando que seja possível executar queries SQL.