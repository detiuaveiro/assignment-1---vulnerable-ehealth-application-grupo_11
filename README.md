# assignment-1---vulnerable-ehealth-application-grupo_11

If you want your instance to be initialized, you have to start from scratch. It is quite easy to do with docker compose when using a named volume like in your case. Warning: this will permanently delete the contents in your db_data volume, wiping out any previous database you had there. Create a backup first if you need to keep the contents.


INICIAR:
flask reset-db
python3 app.py


Vulnerabilidades:

- SQL Injection
    - login -> string (email e pass)
    - doctors -> string (search) e exceção para o html
    - register -> string + executescript
- Cross-Site Scripting (XSS)
    - feedback -> nao tem scape
- Use of Hard-coded Credentials
    - register e login -> hardcoded
- Improper Authentication
    - register como medico
- Unrestricted Upload of File with Dangerous Type
- Uncontrolled Resource Consumption
    - reserved_area -> upload de ficheiros maliciosos e grandes
- Missing Authentication for Critical Function
    - ....


1' AND 1=2 UNION SELECT sql,1,1 FROM sqlite_master WHERE type='table' -- //
1' AND 1=2 UNION SELECT name_, email, password_ FROM app_user -- // 