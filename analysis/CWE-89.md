## CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- https://cwe.mitre.org/data/definitions/89.html

---
## Descrição
SQL Injection é uma vulnerabilidade que permite que um atacante injete código SQL malicioso numa *query*, por intermédio de inputs, cujos valores são guardados numa base de dados relacional. Além disso, os comandos que precedem o código injetado podem ser neutralizados, comprometendo a segurança do sistema, nomeadamente no processo de autenticação.

Está presente em 3 páginas do website:
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
        WHERE app_user.name_ LIKE '%{user_input}%'\
        AND doctor.speciality LIKE '%{speciality}%'"
).fetchall()
```

---
## Explorar a vulnerabilidade

### Login

O utilizador consegue entrar com um email existente e uma password errada, se inserir no campo 'password':
```sql
' or 1=1 ) -- //
```
# TODO -> Mostrar screenshots

Também consegue entrar com o primeiro utilizador da base de dados, se inserir no campo 'password':
```sql
') or 1=1 -- //
```
Neste caso, o primeiro utilizador da base de dados é o **admin**, o qual tem acesso a uma página que permite controlar a base de dados.
# TODO -> Mostrar screenshots
Desta forma, o utilizador consegue aceder a uma conta de outro utilizador, ou gerir a base de dados.

<br>

### Register
Nesta página, o utilizador consegue executar múltiplas *queries* SQL, por exemplo, se inserir no campo 'first_name':
```sql
'); DROP TABLE app_user; -- //
```
# TODO -> Mostrar screenshots


<br>

### Doctors
Nesta página, o utilizador consegue obter todas as tabelas e colunas da base de dados, se inserir na caixa de pesquisa:
```sql
1' AND 1=2 UNION SELECT sql,1,1 FROM sqlite_master WHERE type='table' -- //
```
# TODO -> Mostrar screenshots

Ou obter os nomes, emails e passwords de todos os utilizadores, inserindo na caixa de pesquisa:
```sql
1' AND 1=2 UNION SELECT name_, email, password_ FROM app_user -- //
```
# TODO -> Mostrar screenshots

Com esta vulnerabilidade, o utilizador consegue aceder a **qualquer informação** da base de dados.

---
## Solução

Em SQLite, o '?' é um *placeholder* para um valor passado como argumento de um comando (por exemplo, um INSERT). Essa substituição dinâmica de valores, durante a compilação do comando, é designada por *binding*. Com este mecanismo, o utilizador não consegue injetar código SQL.

Além disso, o uso do método ```executescript``` do módulo ```sqlite3```deve ser evitado, uma vez que permite a execução de múltiplos comandos SQL, favorecendo a vulnerabilidade em questão. Em vez disso, pode e deve ser usado o método ```execute```.

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
        WHERE app_user.name_ LIKE ? \
        AND doctor.speciality LIKE ?" , 
        ('%' + user_input + '%' , '%' + speciality + '%')
).fetchall()
```