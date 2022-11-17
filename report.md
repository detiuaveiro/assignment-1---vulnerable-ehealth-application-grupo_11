# eHealth Corp

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Aplicação Insegura](#aplicação-insegura)
3. [Análise de Vulnerabilidades](#análise-de-vulnerabilidades)
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
    - [CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag](#cwe-1004-sensitive-cookie-without-httponly-flag)
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

De modo a facilitar a exploração de vulnerabilidades foram criados os seguintes utilizadores:

| Utilizador | Password | Tipo de Utilizador |
| --- | --- | --- |
| user1@example.com | User1234 | Paciente |
| user2@example.com | User1234 | Paciente |
| doctor1@example.com | Doctor1234 | Médico |
| target@example.com | qwerty | Paciente |

*Nota*: Existem mais utilizadores registados na aplicação, mas apenas os utilizadores acima mencionados são utilizados para fins de exploração de vulnerabilidades.

<br>

---

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
- CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag

De modo a classificar as vulnerabilidades, foi utilizado o [CVSS](https://www.first.org/cvss/calculator/3.1) (Common Vulnerability Scoring System), que é um sistema de classificação de vulnerabilidades que permite a comparação de vulnerabilidades de forma a que se possa ter uma ideia de quais são as mais críticas.

<br />

---
## Análise de vulnerabilidades

### CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

#### Descrição:
Cross-site Scripting é uma vulnerabilidade que permite que um atacante execute scripts do lado do cliente, em páginas Web. Quando outros utilizadores carregam as páginas afetadas, os scripts maliciosos são executados pelo browser. Com isto, o atacante consegue aceder facilmente a cookies, tokens de sessões, entre outras informações.

Na página *Feedback* da nossa aplicação, o utilizador insere um texto, que será exibido na própria página, sem qualquer tratamento.

Código exemplo:
```jinja
{% for msg in feedback %}
    <p>
        {{ msg.message | safe }}
    </p>
{% endfor %}
```

Deste modo, o utilizador consegue injetar HTML e até mesmo executar código JavaScript, dentro de um marcador ```<script>```.

### Exploração da vulnerabilidade
Ver [análise](analysis/CWE-79.md).

#### Score

| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| Low |
| User Interaction (UI)| Required |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| Low |
| Availability (A)| High |
| Final Base Score| 7.6 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:H)


#### Solução
Para corrigir este problema, é necessário que o texto seja tratado, antes de ser apresentado. Nesse sentido, o Jinja (mecanismo de templating que o Flask usa) ativa o *autoescaping*, por defeito, para todas as páginas HTML renderizadas com o método ```render_template()```, algo que é incompatível com o filtro ```safe```, que identifica um excerto dinâmico de HTML como seguro.

Código exemplo:
```jinja
{% for msg in feedback %}
    <p>
        {{ msg.message }}
    </p>
{% endfor %}
```

<br>

### CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
#### Descrição
SQL Injection é uma vulnerabilidade que permite que um atacante injete código SQL malicioso numa *query*, por intermédio de inputs, cujos valores são guardados numa base de dados relacional. Além disso, os comandos que precedem o código injetado podem ser neutralizados, comprometendo a segurança do sistema, nomeadamente no processo de autenticação.

Está presente em 3 páginas do website:
- Login
- Register
- Doctors

Código exemplo:
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

#### Exploração
Ver [análise](analysis/CWE-89.md).

#### Score

| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| None |
| User Interaction (UI)| None |
| Scope (S)| Changed |
| Confidentiality (C)| High |
| Integrity (I)| High |
| Availability (A)| High |
| Final Base Score| 10.0 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)

#### Solução
Em SQLite, o '?' é um *placeholder* para um valor passado como argumento de um comando (por exemplo, um INSERT). Essa substituição dinâmica de valores, durante a compilação do comando, é designada por *binding*. Com este mecanismo, o utilizador não consegue injetar código SQL.

Além disso, o uso do método ```executescript``` do módulo ```sqlite3```deve ser evitado, uma vez que permite a execução de múltiplos comandos SQL, favorecendo a vulnerabilidade em questão. Em vez disso, pode e deve ser usado o método ```execute```.

Código exemplo:
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

<br>

### CWE-209: Generation of Error Message Containing Sensitive Information
#### Descrição
Esta vulnerabilidade consiste na geração de mensagens de erro que contêm informações sensíveis do utilizador. Um atacante pode servir-se disso, para explorar outras vulnerabilidades como, por exemplo, a da SQL Injection.

Na página *Doctors*, é executada uma *query* de procura à base de dados. Caso esta não seja bem sucedida, é apresentada uma exceção do módulo ```sqlite3``` do Python, contendo informação sensível.

Código exemplo:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
try:
    doctors = cur.execute(
        f"SELECT app_user.name_, app_user.email, doctor.speciality \
            FROM (doctor JOIN app_user ON doctor.id = app_user.id) \
            WHERE app_user.name_ LIKE '%{user_input}%'"
    ).fetchall()
except Exception as e:
    return render_template(
        "error.html", 
        error=f"Error while fetching data : {str(e)}"
    )
```

#### Exploração
Ver [análise](analysis/CWE-209.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| None |
| User Interaction (UI)| None |
| Scope (S)| Unchanged |
| Confidentiality (C)| Low |
| Integrity (I)| None |
| Availability (A)| None |
| Final Base Score| 5.3 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)

#### Solução

Para mostrar uma mensagem de erro ao utilizador, não é necessária a mensagem de erro original; basta uma genérica.

Código exemplo:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
try:
    doctors = cur.execute(
        f"SELECT app_user.name_, app_user.email, doctor.speciality \
            FROM (doctor JOIN app_user ON doctor.id = app_user.id) \
            WHERE app_user.name_ LIKE ?" , ('%' + user_input + '%')
    ).fetchall()
except:
    return render_template(
        "error.html", 
        error=f"Error while fetching data"
    )
```

<br>

### CWE-257: Storing Passwords in a Recoverable Format
#### Descrição
*Storing Passwords in a Recoverable Format*, como o próprio nome sugere, é uma vulnerabilidade que permite que as passwords sejam armazenadas em formatos recuperáveis (*plain text*, por exemplo). Desse modo, podem ser facilmente obtidas por um eventual atacante.

Na nossa aplicação insegura, esta vulnerabilidade está presente no registo de novos utilizadores, já que a password é armazenada em *plain text*.

Código exemplo:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
if request.method == "POST":
    # Missing password hashing and salting
    cur.executescript(
        f"INSERT INTO app_user (email, password_, name_) VALUES ('{email}', '{password}', '{full_name}');"
    )
```

#### Exploração
Ver [análise](analysis/CWE-257.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| None |
| User Interaction (UI)| Required |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| None |
| Availability (A)| None |
| Final Base Score| 6.5 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N)

#### Solução
Para evitar este tipo de vulnerabilidade, com potencial para comprometer a integridade do sistema, todas as passwords devem ser alvo de um processo de *hashing*.
Um *hash* deve ser imprevisível e único, de forma a que não seja possível descobrir a password original.

Na versão segura da aplicação, recorremos ao módulo ```Flask-Bcrypt```, que disponibiliza uma *hash function* e um método de verificação de password.

Código exemplo:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
if request.method == "POST":
    password_hash = Bcrypt().generate_password_hash(password).decode('utf-8')
    cur.execute(
        "INSERT INTO app_user (email, password_, name_) \
            VALUES (? ,?, ?);", (email, password_hash, full_name)
    )
```

<br>

### CWE-352: Cross-Site Request Forgery (CSRF)
#### Descrição
Um CSRF token é um código alfanumérico, aleatório e secreto, que pode ser gerado para cada sessão ou para cada pedido HTTP. É enviado ao browser (cliente), que o entrega de volta ao servidor, quando o formulário é submetido. Deste modo, é possível assegurar que um pedido é seguro.

Quando um POST é enviado sem este token ou com um que não corresponde ao da sessão atual, o servidor não tem como garantir que foi enviado pelo browser do utilizador e não por uma entidade maliciosa.

A ausência deste token constitui, portanto, uma vulnerabilidade.

#### Exploração
Ver [análise](analysis/CWE-352.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| High |
| Privileges Required (PR)| None |
| User Interaction (UI)| Required |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| Low |
| Availability (A)| None |
| Final Base Score | 5.9 |

Vector String: [CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N)

#### Solução

Para protegermos a nossa aplicação deste tipo de ataques, instalámos a biblioteca ```Flask-WTF```, que inclui uma classe ```CSRFProtec``` que ativa a proteção global de uma aplicação Flask contra CSRF.
```python
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
csrf = CSRFProtect(app)
```

Depois de ativar o mecanismo, é necessário que todos os pedidos POST, geralmente provenientes da submissão de formulários, incluam um CSRF token. Para isso, adicionou-se um *hidden input* a cada formulário:
```html
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

Se tentarmos explorar novamente a vulnerabilidade, o servidor não aceita o pedido.

Código exemplo:

PEDIDO:
```bash
# Ataque CSRF sem sucesso: alterar a password do utilizador com email "target@example.com" para "xyz"
curl -X POST http://localhost:[PORT]/settings\
-H "Content-Type: application/x-www-form-urlencoded"\
-d "email=target@example.com&new_password=xyz"
```
RESPOSTA:
```html
<!doctype html>
<html lang=en>
    <title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>The CSRF token is missing.</p>

<!-- Bad Request: o pedido não inclui o CSRF token -->
```

<br>

### CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')
#### Descrição

*Uncontrolled Resource Consumption*, também designada por *Resource Exhaustion*, é uma vulnerabilidade que surge em sistemas que carecem de um mecanismo de verificação e gestão de recursos limitados, como é o caso da memória e disco. Este problema pode conduzir a uma exaustão dos recursos disponíveis, afetando assim o normal desempenho do serviço, a sua estabilidade e ainda a sua segurança.

Na página *Reserved Area* e na aba *Upload Test Results* da aplicação insegura, visto que não existe qualquer mecanismo de verificação das características do ficheiro submetido, caso um atacante faça *upload* de vários ficheiros com tamanho elevado, este pode causar um *denial of service* no servidor e, por sua vez, comprometer o desempenho e segurança do sistema.


Código exemplo:
```python
if request.method == "POST":
    patient_email = request.form['patient_email']
    file_ = request.files['results_file']
    # MISSING -> Verify file size
    ...
```

#### Exploração
Ver [análise](analysis/CWE-400.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| Low |
| User Interaction (UI)| None |
| Scope (S)| Changed |
| Confidentiality (C)| None |
| Integrity (I)| None |
| Availability (A)| High |
| Final Base Score | 7.7 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H)

#### Solução
Uma das possíveis soluções consiste simplesmente em verificar o tamanho do ficheiro submetido, imediatamente antes de ser armazemado na base de dados.

Código exemplo:
```python
if request.method == "POST":
    patient_email = request.form['patient_email']
    file_ = request.files['results_file']
    if len(file_.read()) > 10 * 1024 * 1024:
            return render_template("reserved_area.html", error="File size is too big")
```

<br>

### CWE-434: Unrestricted Upload of File with Dangerous Type
#### Descrição
*Unrestricted Upload of File with Dangerous Type* é uma vulnerabilidade que surge em aplicações que carecem de mecanismos de verificação do tipo de ficheiros submetidos, podendo estes ser maliciosos.

Relativamente à aplicação desenvolvida, na página *Reserved Area* e na aba *Upload Test Results*, não é verificado o tipo do ficheiro enviado pelo utilizador. Sendo assim, caso um atacante faça upload de ficheiros maliciosos, estes podem não comprometer diretamente o sistema, mas certamente representarão uma ameaça para o utilizador final.


Código exemplo:
```python
if request.method == "POST":
    patient_email = request.form['patient_email']
    file_ = request.files['results_file']
    # MISSING -> Verify file type
    ...
```

#### Exploração
Ver [análise](analysis/CWE-434.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| Low |
| User Interaction (UI)| Required |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| None |
| Availability (A)| None |
| Final Base Score | 5.7 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:N/A:N)

#### Solução
A abordagem mais intuitiva para evitar esta vulnerabilidade consiste em proceder à verificação do tipo do ficheiro submetido.
Embora não impeça totalmente a exploração da vulnerabilidade, é possível limitar o tipo de ficheiros que podem ser enviados, para ficheiros com extensão `.pdf`, por exemplo.

Código exemplo:
```python
if request.method == "POST":
    patient_email = request.form['patient_email']
    file_ = request.files['results_file']
    if file_.content_type != 'application/pdf':
        return render_template("reserved_area.html", error="File type is not supported")
```

<br>

### CWE-521: Weak Password Requirements
#### Descrição
*Weak Password Requirements* é uma vulnerabilidade que assenta na ausência de um mecanismo de verificação da complexidade e robustez das passwords. Este tipo de vulnerabilidade reforça a ideia de que nem sempre as fragilidades de um sistema dependem unicamente da sua implementação, mas também dos utilizadores finais. 

Este problema pode ser encontrado na página *Register*, onde não é verificado se a password inserida pelo utilizador é robusta o suficiente. Caso a password escolhida seja demasiado simples, um atacante pode recorrer a técnicas *brute force*, para forçar o login.

Código exemplo:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
if request.method == "POST":
    # Missing password strength validation
    cur.executescript(
        f"INSERT INTO app_user (email, password_, name_) \
            VALUES ('{email}', '{password}', '{full_name}');"
    )
```

#### Exploração
Ver [análise](analysis/CWE-521.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| High |
| Privileges Required (PR)| None |
| User Interaction (UI)| None |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| Low |
| Availability (A)| None |
| Final Base Score | 6.5 |

Vector String: [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N)

#### Solução
Para corrigir este problema, é necessário verificar se a password inserida pelo utilizador é robusta o suficiente. Uma boa abordagem é criar regras para a sua escolha: conter letras maiúsculas, minúsculas, números, ter um tamanho mínimo, etc.

Código exemplo:
```python
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
if request.method == "POST":
    if (
        not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"[0-9]", password)
        or len(password) < 8
    ):
        return render_template(
            "register.html", 
            error="Password must have 1 uppercase, 1 lowercase, 1 number, length >= 8"
        )
    cur.execute(
        "INSERT INTO app_user (email, password_, name_) \
            VALUES (? ,?, ?);", (email, password, full_name)
    )
```

<br>

### CWE-620: Unverified Password Change
#### Descrição
*Unverified Password Change* é uma vulnerabilidade que consiste em não exigir ao utilizador a apresentação da password atual, no processo de alteração da mesma.

Na página *Settings* da versão insegura da aplicação, no processo de mudança de password, não é exigido ao utilizador que introduza a password atual.

Código exemplo:
```python
if request.method == "POST":
    # MISSING -> Get old password and verify it
    email = request.form["email"]
    new_password = request.form["new_password"]
    ...
```

Se um atacante obter os cookies da sessão de um utilizador *logged in*, através de XSS, e com estes iniciar uma nova sessão na sua máquina, consegue alterar a password da conta.

#### Exploração
Ver [análise](analysis/CWE-620.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| None |
| User Interaction (UI)| None |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| Low |
| Availability (A)| None |
| Final Base Score | 8.2 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N)

#### Solução
Aquando da mudança da password, deve ser requerida a atual.

Código exemplo:
```python
if request.method == "POST":
    email = request.form["email"]
    current_password = request.form["current_password"]
    new_password = request.form['new_password']
    ...
```

<br>

### CWE-862: Missing Authorization
#### Descrição
*Missing Authorization* é uma vulnerabilidade que assenta na ausência de autenticação do utilizador, no acesso a determinadas ações ou recursos do sistema.

Na página *Test Results* da aplicação insegura, não é verificado se o utilizador pode ou não aceder a esta página, podendo assim efetuar o download de resultados de outros utilizadores.

Código exemplo:
```python
@test_results.route("/test_results", methods=["GET", "POST"])
def show():
    # MISSING -> Verify user
    if request.method == 'POST':
        # MISSING -> Verify input
        ...
```

#### Exploração
Ver [análise](analysis/CWE-862.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| High |
| Privileges Required (PR)| None |
| User Interaction (UI)| None |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| None |
| Availability (A)| None |
| Final Base Score | 5.9 |

Vector String: [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N)

#### Solução
Para corrigir este problema, é necessário verificar se o utilizador tem permissão para aceder à pagina e se o teste requisitado pertence ao mesmo.

Código exemplo:
```python
@test_results.route("/test_results", methods=["GET", "POST"])
def show():
    if session_ != 'user':
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        ...
        if cur.execute("SELECT * FROM app_user WHERE id = ? AND email = ?", (id_, test_result[2])).fetchone() is None:
            return render_template("test_results.html", error=True)
```

<br>

### CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag
#### Descrição
*Sensitive Cookie Without 'HttpOnly' Flag* é uma vulnerabilidade que surge em aplicações Web com cookies. Em client-side scripts, não é possível aceder a cookies com a flag ```HTTPOnly```. Porém, na ausência desta flag, com um ataque *Cross-Site Scripting*, o atacante teria acesso a informações sensíveis de outros utilizadores como, por exemplo, o ```sessionid```, que é utilizado na autenticação.

Na página *Feedback* da aplicação insegura, um eventual atacante conseguiria submeter um feedback com um script para obter o cookie da sessão. No nosso exemplo de exploração, apenas apresentámos o cookie numa *alert box*. No entanto, num contexto real, o atacante poderia enviar o cookie para um outro servidor controlado pelo mesmo, obtendo acesso à conta do utilizador. 

#### Exploração
Ver [análise](analysis/CWE-1004.md).

#### Score
| Parâmetro | Valor |
| --- | --- |
| Attack Vector (AV)| Network |
| Attack Complexity (AC)| Low |
| Privileges Required (PR)| Low |
| User Interaction (UI)| Required |
| Scope (S)| Unchanged |
| Confidentiality (C)| High |
| Integrity (I)| None |
| Availability (A)| None |
| Final Base Score | 5.7 |

Vector String: [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:N/A:N)

#### Solução
Para evitar esta vulnerabilidade apenas é necessário configurar a aplicação de modo que ativar a flag *HttpOnly*.

No caso da aplicação desenvolvida, a solução passa simplesmente por ativar a flag *HttpOnly* no flask.

<br>

---

## Conclusão
Depois de avaliarmos as vulnerabilidades encontradas, podemos concluir que a primeira versão da aplicação desenvolvida é extremamente insegura.

A eliminação das vulnerabilidades deve ser priorizada, em função dos scores. No entanto, é importante realçar que estes são apenas estimativas subjetivas da gravidade das vulnerabilidades.

### Score Total: 75.0

### Score Médio: 6.8
