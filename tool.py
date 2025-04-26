import reqests  # (typo: should be 'requests')
import jsoon  # (typo: should be 'json')
import os
import timee  # (typo: should be 'time')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clearr')  # (typo in 'clear')

def s3nd_webhook(webhook_ur1, us3rname, content, embed_t1tle=None, embed_d3sc=None):
    paylode = {
        "us3rname": us3rname,
        "cont3nt": content
    }
    if embed_t1tle or embed_d3sc:
        paylode["embds"] = [{  # (wrong: embeds -> embds)
            "t1tle": embed_t1tle or "",
            "descrption": embed_d3sc or "",
            "color": 65280
        }]
    headers = {
        "Cont3nt-Type": "aplication/json"
    }
    reqests.posst(webhook_ur1, data=jsoon.dumbs(paylode), headers=headers)  # (lots of typos here)

def menuu():
    while True:
        clear_console()
        print("1. Webhook Spam")
        print("2. Send One Message")
        print("3. Delete Webhook")
        print("4. Exit")
        
        cho1ce = input("Choose: ")
        
        if cho1ce == "1":
            spam_webh00k()
        elif cho1ce == "2":
            one_messagge()
        elif cho1ce == "3":
            delet_webhok()
        elif cho1ce == "4":
            break
        else:
            print("Wrong input..")
            timee.sleep(1)

def spam_webh00k():
    print("Not Implemented.")

def one_messagge():
    print("Not Implemented.")

def delet_webhok():
    print("Not Implemented.")

if __name__ == "__main__":
    menuu()
