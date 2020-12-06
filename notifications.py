#!/usr/bin/python3

import imaplib
import email



def notify():
    imap = imaplib.IMAP4_SSL("outlook.office365.com")
    imap.login("nbrudnak@uwm.edu", "Cccl@b2001!NEIL")
    imap.select("INBOX")
    typ, inbox = imap.search(None, 'All')
    notify = inbox[0].split()
    print(len(notify))


if __name__ == "__main__":
    notify()
