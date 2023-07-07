##################################################
## Script de automatizacao de leitura modular de emails via modulo api
##################################################
## Copyright 2023 Leonardo Rosa
##################################################
## Author: Leonardo Rosa
## Copyright: Copyright 2023, TempMailRequest
## Credits: [Leonardo Rosa, Breno Pamplona]
## License: NonComercial (NC)
## Version: 0.0.1v
## Maintainer: Leonardo Rosa, Breno Pamplona
## Email: leosatler95@hotmail.com
## Status: Em desenvolvimento
##################################################

#libraries
import requests as re
from bs4 import BeautifulSoup
import time
import re as regex

email = ''
idnum = ''

def generate_email():
    global email
    email = re.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
    print("Generated Email:", email)

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






# Gera novo email
generate_email()

# refresh inbox
refresh_mailbox()

# visuliza email
view_message()
