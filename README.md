# assignment-1---vulnerable-ehealth-application-grupo_11

README.md: contains the project description, authors, enumerates vulnerabilities implemented.


## Grupo de desenvolvimento
Pedro Rodrigues (102778)
Rafael Gonçalves (102534)
Leonardo Almeida (102536)
Anzhelika [INSERT]


## Organização do projeto
- ```app```: contains the insecure application, including instructions to run it (Docker is recommended);
- ```app_sec```: contains the secure application, including instructions to run it (Docker is recommended);
- ```report```: contains a document (PDF, MD) describing the project, the vulnerabilities with their score and fix;
- ```analysis```: contains scripts/textual descriptions/logs/screen captures demonstrating the exploration of each vulnerability;
- ```README.md```: contains the project description, authors, enumerates vulnerabilities implemented.

<br />

## Execução do projeto
docker build -t app .
docker build -t app_sec .


CWE-352: Cross-Site Request Forgery (CSRF)
- https://cwe.mitre.org/data/definitions/352.html
- https://testdriven.io/blog/csrf-flask/