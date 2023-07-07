# TempMailApiRequests
Script para solicitacoes de email temporario e funcionalidade modular para aquisicao de codigo de verificacao.

```python def generate_email():
    global email
    email = re.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
    print("Generated Email:", email)```
