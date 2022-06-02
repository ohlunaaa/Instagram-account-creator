import os
import requests
import random
import secrets
import time
from user_agent import generate_user_agent

print("""
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                          
""")
token = "" # add your 5sim api token here
headers187 = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}
timer = 0
def passwords():
    chars = "abcdefghijklmnopqrstuvwxytABDOWEITJ"
    number = 6 
    length = 8
    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)
    return passwords

def gen():
    while True:
        Ideee= 'X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
        r      = requests.Session()
        cookie = secrets.token_hex(8)*2
        momy = requests.get('https://5sim.net/v1/user/profile', headers=headers187).json()
        your_mail = momy["email"]
        b = momy["balance"]
        momy2 = requests.get('https://5sim.net/v1/user/buy/activation/russia/any/instagram', headers=headers187).json()
        phone_id = momy2["id"]
        phone_number = momy2["phone"]
        price = momy2["price"]
        phone  = phone_number
        phoneid = phone_id
        user   = passwords()
        paas   = passwords()
        name   = 'By @a404ontop'
        headers   = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : generate_user_agent(),
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
        }

        data1   = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'client_id': Ideee,
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'fals'
        }
        data2   = {
            'client_id': Ideee,
            'phone_number': phone,
            'phone_id': '',
            'big_blue_token': ''
        }
        req1 = r.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=headers,data=data1)
        req2 = r.post('https://www.instagram.com/accounts/send_signup_sms_code_ajax/',headers=headers,data=data2)
        if 'Looks like your phone number may be incorrect.' in req2.text:
            print('Error')
            exit()
        elif 'Please wait a few minutes before you try again.' in req2.text:
            print('Please wait a few Minutes')
            exit()
        elif 'true' in req2.text:
            print('sending sms')
            pass
        else:
            print('Error ..')
            exit()
        timer = 0
        while timer < 30:
            time.sleep(3)
            momy420 = requests.get('https://5sim.net/v1/user/check/' + str(phone_id), headers=headers187).json()
            if momy420["status"] == "RECEIVED":
                if momy420["sms"]:
                    sms = momy420["sms"][0]["code"]
                    code = sms
                    data3 = {
                        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
                        'phone_number': phone,
                        'username': user,
                        'first_name': name,
                        'month': '1',
                        'day': '1',
                        'year': '1999',
                        'sms_code': code,
                        'client_id': Ideee,
                        'seamless_login_enabled': '1',
                        'tos_version': 'row'
                    }
                    req3 = r.post('https://www.instagram.com/accounts/web_create_ajax/',headers=headers,data=data3)
                    if "That code isn't valid." in req3.text:
                        print("That code isn't valid")
                        exit()
                    elif 'true' in req3.text:
                        print("Done Created Account")
                        file = open("accounts.txt","a")
                        file.write(f"{user}:{paas}:{phone}\n")
                        pass
                    elif "checkpoint_required" in req3.text:
                        print(' Done')
                        pass
                    else:
                        print(f"Usernam: {user}")
                        print(f"password: {paas}")
                        with open('user.txt', 'w') as f:
                            f.write(f'{phone}:{user}:{paas}')
            else:
                timer += 1
                print("Waiting for code ")
        
gen()
