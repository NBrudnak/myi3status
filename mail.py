#!/usr/bin/python3
import imaplib
import email


def login():
    while True:
        user=input("username:")
        password=input("password:")

        imap = imaplib.IMAP4_SSL("outlook.office365.com")
        user.rstrip()
        password.rstrip()
        try:
            imap.login(user,password)
            print("login successful!")
            return imap
        except:
            print("username or password is incorrect ):")


def mailboxSelector(imap, limiter):
    imap.select("INBOX")
    typ, inbox = imap.search(None, 'ALL')
    correctList = inbox[0].split()
    correctList = correctList[len(correctList)-limiter:]
    return correctList

def listMessages(correctList, imap):
    
    count = 0
    for i in correctList:
        count+=1
        typ, inbox = imap.fetch(i, '(RFC822)')
        try:
            msg = email.message_from_string(inbox[0][1].decode('utf-8'))
            print(count)
            print(msg['from'])
            print(msg['subject'])
        except:
            print("unable to print email ===============================")

    return correctList


def emailSelect(correctList, imap):

    while(True):
        command = input("\n==================\n\nenter email to view: ").split()
        if command[0] == "v":
            typ, inbox = imap.fetch(correctList[int(command[1])], '(RFC822)')
            try:
                msg = email.message_from_string(inbox[0][1].decode('utf-8'))
                for m in msg.walk():
                    if m.get_content_type() == "text/plain":
                        body=m.get_payload()
                        print(body)

            except:
                print("unable to print email ===============================")
        


if __name__ == "__main__":
    imap = login()
    correctList = mailboxSelector(imap, 10)
    listMessages(correctList, imap)
    emailSelect(correctList, imap)




"""
  for p in message.walk():i
      if p.get_content_type() == "text/plain":
          body=p.get_payload()
 print(body)"""
