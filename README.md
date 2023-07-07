# TempMailApiRequests

<p>Script para solicitacoes de email temporario e funcionalidade modular para aquisicao de codigo de verificacao<p>
    
## Dependecias necessarias para utilizar o programa:

<p>Criei um arquivo requirements.txt que abrange todas as dependencias necessarias para rodar o programa de uma maneira simple tendo que somente fazer uma instalacao manual</p>

> ### Aqui de encontra um passo a passo de como fazer a instalação dessas dependências com um simples comando.
>
> - Depois de baixar os arquivos do Github, abra-os em seu editor de texto e verifique no terminal se você está dentro do diretório correto, conforme o exemplo abaixo:
>
> ![codesnippet](https://github.com/leosatler/TempMailApiRequests/assets/67660351/aec4e8d9-06ea-44dc-855c-1dfc033fc8a7)
>
> - Instale as dependências usando o comando pip:
>
> ```
> pip install -r requirements.txt
> ```
>
> **Esse comando instalará todas as dependências necessárias para rodar o programa de uma vez só, sem ter que gastar tempo instalando uma por uma.**

    
### Funcao responsavel por criar email temporario:
```python
    def generate_email():
    global email
    email = re.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
    print("Generated Email:", email)
```
### Funcao que refresca a pagina buscando a entrega de email corespondente ao endereco de email criado pela funcao acima:
```python
def refresh_mailbox():
    if email == '':
        print("Generate an email first.")
    else:
        while True:
            getmsg_endp = "https://www.1secmail.com/api/v1/?action=getMessages&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:]
            print("Get Messages Endpoint:", getmsg_endp)
            try:
                response = re.get(getmsg_endp)
                print("Response:", response.text)
                ref_response = response.json()
                if ref_response:
                    global idnum
                    idnum = str(ref_response[0]['id'])
                    from_msg = ref_response[0]['from']
                    subject = ref_response[0]['subject']
                    refreshrply = 'You have a message from ' + from_msg + '\n\nSubject: ' + subject
                    print("Refresh Reply:", refreshrply)
                    break
                else:
                    print("No messages yet. Waiting for new messages...")
                    time.sleep(5) 
            except Exception as e:
                print("Error occurred while retrieving messages:", str(e))
                break
```
### Funcao que visualiza o sujeito e corpo do email e nessa versao tambem procura o *codigo de ativacao*
```python
def view_message():
    if email == '':
        print("Generate an email first.")
    else:
        if idnum == '':
            print("Retrieve a message ID first.")
        else:
            msg = re.get("https://www.1secmail.com/api/v1/?action=readMessage&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + idnum).json()
            if not msg:
                print("No messages found.")
                return
            subject = msg['subject']
            mailbox_view = 'From: ' + msg['from']
            print(mailbox_view)
            print("Subject: " + subject)
            code = regex.search(r'\d+', subject).group()
            print("Code: " + code)
```
