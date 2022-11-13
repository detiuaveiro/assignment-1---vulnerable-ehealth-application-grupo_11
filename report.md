
For all vulnerabilities:

    Vulnerabilities should be distinct and have distinct CWEs;
    The CWE must be identified;
    The implementation must follow the logic and purpose of the application. That is, no page with the single purpose of showing the vulnerability;
    Students should be able to demonstrate the vulnerability in a report with scripts/screenshots;
    It is preferred to have vulnerabilities that result from bad patterns instead of those resulting from something that is missing. Avoid things like absence of brute force protection/access control/encryption/logging


report: contains a document (PDF, MD) describing the project, the vulnerabilities with their score and fix;








Vulnerabilidades:

- CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
    - https://cwe.mitre.org/data/definitions/89.html

    - login -> string (email e pass)
    - doctors -> string (search) e exceção para o html
    - register -> string + executescript

- CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    - https://cwe.mitre.org/data/definitions/79.html

    - feedback -> nao tem scape

- CWE-798: Use of Hard-coded Credentials
    - https://cwe.mitre.org/data/definitions/798.html

    - register e login -> hardcode

- CWE-287: Improper Authentication
    - https://cwe.mitre.org/data/definitions/287.html

    - register como medico

- CWE-434: Unrestricted Upload of File with Dangerous Type
    - https://cwe.mitre.org/data/definitions/434.html

    - reserved_area -> upload de ficheiros maliciosos

- CWE-400: Uncontrolled Resource Consumption 
    - https://cwe.mitre.org/data/definitions/400.html

    - reserved_area -> upload de ficheiros grandes

- CWE-862: Missing Authorization
    - https://cwe.mitre.org/data/definitions/862.html

    - test_results -> nao tem autenticação e codigo do ficheiro é facil

- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
    - https://cwe.mitre.org/data/definitions/200.html

    - test_results 

- CWE-20: Improper Input Validation
    - https://cwe.mitre.org/data/definitions/20.html

    - sql injection e cross site scripting

- CWE-522: Insufficiently Protected Credentials
    - https://cwe.mitre.org/data/definitions/522.html

    - sql injection e login

- CWE-306: Missing Authentication for Critical Function
    - https://cwe.mitre.org/data/definitions/306.html

    - sql injection no login