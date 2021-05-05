import os,sys
import requests
import random
from time import sleep
os.system("clear")
count=0


print('''
                              
          ,     ,
         (\____/)
          (_oo_)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__\
     (\   /____\

                                                            
_|_  o |__,     _|_   __  |__, 
 |_, | |  \      |_, (__) |  \  
 
Telegram : @Professional_school
Github : iraq-hacker                                
                               
                               
''')

rek = input('''

1 - TikTok-Checker - Checker Turbo -!
2 - Turbo-Tiktok -_×
3 - create users ~_~

ُEnter Number:''')
   
if rek =="1":
    bb = input('''
        1 - Normal Cheacker
        2 - Cheacker with Turbo
          └──=> Enter Number : ''')
    if bb=='1':
        dd = input ('username list : ')
        if dd==''or'':
            dd='user.txt'
        print ( """│
        └──=> { Extracting session id through Burp Suite Or from the Chrome browser } """)
        sessionId = input("   "
                          "                       └──=> sessionid : ")
        if sessionId==""or"":
            print(f"Make sure to put the seam in hand")
        if dd =="1"or " ":
            password = open(dd).read().splitlines()

            for password in password:
                  url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+password+"&app_language=ar"
                  payload = ""
                  headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "Connection": "close",
                    "Host": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Cache-Control": "max-age=0"


            }
                  cookies = {'sessionid': sessionId}
                  response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
                  post = str (response.json ()["status_msg"])
                  if post==""or"":
                      count += 1
                      print("{}: {}".format(count, password.strip())+" |  found  ")
                      with open('accountfound.txt', 'a') as x:
                          x.write(password + '\n')
                  elif post=="Your login has expired":
                      print(f'''
You must be registered with your account
 and the volume is in the hands of the account right yet 
Any problem contact me telegram : @ iiwiw
                      ''')
                      exit()
                  else:
                      count += 1
                      print("{}: {}".format(count, password.strip())+" | not available |  ")
    if bb=='2':
        sessionop= input('Enter sessionid for cheaker: ')
        ssa = input("Enter session id list : ")
        sessiones = open(ssa).read().splitlines()
        name = input("Enter user list : ")
        names = open(name).read().splitlines()
        req = requests.sessions
        for names in names:
            if names == None:
                print("End users !!")
                exit()
            url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + names + "&app_language=ar"
            payload = ""
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"

            }

            cookies = {'sessionid': sessionop}
            response = requests.request("GET", url, data=payload, headers=headers, cookies=cookies)
            post = str(response.json()["status_msg"])
            if post == "" or "":
                for sessiones in sessiones:
                    count += 1
                    print( "{}: {}".format(count,  names.strip())  + " |  found  ")
                    url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'

                    head1 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessiones}',
                        "x-tt-passport-csrf-token": f"{sessiones}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
                    }

                    data = {
                        'login_name': f'{names}'
                    }
                    WeeX = requests.post(url, data=data, headers=head1).text
                    if '"message":"success"' in WeeX:
                        with open('accounts_Swap.txt', 'a') as x:
                            x.write(names +' Swap by @WeeX0'+ '\n')
                        print(f'{sessiones}الى {names}The transfer has been completed ')
                    elif '"description":"You are visiting our service too frequently."' in WeeX:
                        print('runVPN')
                        print('Try again in 10 seconds')
                        sleep(10)
                    elif '"description":"The conversation has expired, please log in again"' in WeeX:
                        print(f'!!Session id Error --> {sessiones}')

                    elif '"description":"login name can only be updated once within one month."' in WeeX:
                        print(f'  {sessiones}You can not choose until after a month ')
                        print('Choose another account ')

                    elif '"message":"error"' in WeeX:
                        print("wait")


            elif post == "Your login has expired":
                print(f'''
You must be registered with your account, 
and the volume is in the hands of the account right after any problem
, contact me
                        telegram : iiwiw
                        
                  ''')
                exit()
            else:
                count += 1
                print( "{}: {}".format(count,  names.strip())  + " | not available |  ")
if rek =="2":
    ssa = input("Enter session id : ")
    name = input("Enter Target : ")
    req = requests.sessions
    url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'

    head1 = {
        'Host': 'api16-normal-c-alisg.tiktokv.com',
        'Connection': 'close',
        'Content-Length': '25',
        'Cookie': f'sessionid={ssa}',
        "x-tt-passport-csrf-token": f"{ssa}",
        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sdk-version': '2',
        'passport-sdk-version': '5.12.1'
    }

    data = {
        'login_name': f'{name}'
    }
    while True:
        WeeX = requests.post(url, data=data, headers=head1).text
        if '"message":"success"' in WeeX:
            print('The transfer has been completed')
        elif '"description":"You are visiting our service too frequently."' in WeeX:
            print('')
            print('Try again in 10 seconds')
            sleep(10)
        elif '"description":"The conversation has expired, please log in again"' in WeeX:
            print('!!Session id Error ')
            exit()
        elif '"description":"login name can only be updated once within one month."' in WeeX:
            print('!You can not choose until after a month')
            print('Choose another account ')
        elif '"message":"error"' in WeeX:
            print("wait")
if rek =="3":
    print("___________________         ")
    print("1- Three letters and ( - )")
    print("2- Three letters and (. )")
    print("3- Three random characters")
    print("4- Three")
    print("5- Three without numbers")
    print("6- Quadrant")
    print("7- Quadrant without numbers")

    print("4.Custom")
    sa = input("Choose")

    if sa == "1":

        print("Her place")
        print("1| (_***)")
        print("2| (*_**)")
        print("3| (**_*)")
        print("4| (***_)")
        da = input("Choose")
        if da == "1":
            uesr = '_'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''

                for item in range(length2):
                    password = ''
                for item in range(length2):
                    password += random.choice(chars2)
                bb = uesr + password
                print(bb)
                with open('user.txt', 'a') as x:
                    x.write(bb + '\n')
        if da == "2":
            uesr = '_'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''

                for item in range(length2):
                    password = ''
                for item in range(length2):
                    password = random.choice(chars2)
                for item in range(2):
                    password1 = ''
                for item in range(2):
                    password1 += random.choice(chars2)
                ba = password + uesr + password1

                print(ba)
                with open('user.txt', 'a') as x:
                    x.write(ba + '\n')

        if da == "3":
            uesr = '_'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''

                for item in range(2):
                    password = ''
                for item in range(2):
                    password += random.choice(chars2)
                for item in range(1):
                    password1 = ''
                for item in range(1):
                    password1 += random.choice(chars2)
                bd = password + uesr + password1

                print(bd)
                with open('user.txt', 'a') as x:
                    x.write(bd + '\n')
        if da == "4":
            uesr = '_'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''
                for item in range(3):
                    password = ''
                for item in range(3):
                    password += random.choice(chars2)

                bc = password + uesr

                print(bc)
                with open('user.txt', 'a') as x:
                    x.write(bc + '\n')
    if sa == "2":
        print("status")
        print("1| .***")
        print("2| *.**")
        print("3| **.*")
        da = input("type :")
        if da == "1":
            uesr = '.'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''

                for item in range(length2):
                    password = ''
                for item in range(length2):
                    password += random.choice(chars2)
                bb = uesr + password
                print(bb)
                with open('user.txt', 'a') as x:
                    x.write(bb + '\n')
        if da == "2":
            uesr = '.'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''

                for item in range(length2):
                    password = ''
                for item in range(length2):
                    password = random.choice(chars2)
                for item in range(2):
                    password1 = ''
                for item in range(2):
                    password1 += random.choice(chars2)
                ba = password + uesr + password1

                print(ba)
                with open('user.txt', 'a') as x:
                    x.write(ba + '\n')

        if da == "3":
            uesr = '.'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
            amount = input('How many user')
            amount = int(amount)

            length2 = 3
            length2 = int(length2)

            for password in range(amount):
                password = ''

                for item in range(2):
                    password = ''
                for item in range(2):
                    password += random.choice(chars2)
                for item in range(1):
                    password1 = ''
                for item in range(1):
                    password1 += random.choice(chars2)
                bd = password + uesr + password1

                print(bd)
                with open('user.txt', 'a') as x:
                    x.write(bd + '\n')
    if sa == "3":
        uesr = '.'  
        chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  
        amount = input('How many user')
        amount = int(amount)
        length2 = 3
        length2 = int(length2)

        for password1 in range(amount):
            password1 = ''
            for item in range(length2):
                password1 = ''
            for item in range(length2):
                password1 += random.choice(chars2)
            password35 = "." + password1

            password2 = ''

            for item in range(length2):
                password2 = ''
            for item in range(length2):
                password2 = random.choice(chars2)
            for item in range(2):
                password3 = ''
            for item in range(2):
                password3 += random.choice(chars2)
            password27 = password2 + "." + password3

            password4 = ''

            for item in range(2):
                password4 = ''
            for item in range(2):
                password4 += random.choice(chars2)
            for item in range(1):
                password5 = ""
            for item in range(1):
                password5 += random.choice(uesr)
            for item in range(1):
                password99 = ''
            for item in range(1):
                password99 += random.choice(chars2)
                password9 = password4 + password5 + password99

            useer = '_'  
            chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'  

            for password109 in range(amount):
                password109 = ''
                for item in range(length2):
                    password109 = ''
                for item in range(length2):
                    password109 += random.choice(chars2)
                password350 = "_" + password109

                password20 = ''
                for item in range(length2):
                    password20 = ''
                for item in range(length2):
                    password20 = random.choice(chars2)
                for item in range(2):
                    password30 = ''
                for item in range(2):
                    password30 += random.choice(chars2)
                password270 = password20 + "_" + password30

                password40 = ''

                for item in range(2):
                    password40 = ''
                for item in range(2):
                    password40 += random.choice(chars2)
                for item in range(1):
                    password50 = ""
                for item in range(1):
                    password50 += random.choice(useer)
                for item in range(1):
                    password990 = ''
                for item in range(1):
                    password990 += random.choice(chars2)
                    password90 = password40 + password50 + password990

                password60 = ''
                for item in range(3):
                    password60 = ''
                for item in range(3):
                    password60 += random.choice(chars2)
                    password100 = password60 + "_"

            mylist = [password9, password27, password35, password100, password90, password270, password350]
            passwordff = ""
            ddd = passwordff + random.choice(mylist)
            print(ddd)
            with open('user.txt', 'a') as x:
                x.write(ddd + '\n')
    if sa == "4":
        uesr = ''  
        chars2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'  
        amount = input('How many user')
        amount = int(amount)

        length2 = int(3)

        for password in range(amount):
            password = ''

            for item in range(length2):
                password = ''
            for item in range(length2):
                password += random.choice(chars2)

            print(password)
            with open('user.txt', 'a') as x:
                x.write(uesr + password + '\n')
    if sa == "5":
        uesr = ''  
        chars2 = 'qwertyuiopasdfghjklzxcvbnm'  
        amount = input('How many user')
        amount = int(amount)
        length2 = int(3)

        for password in range(amount):
            password = ''

            for item in range(length2):
                password = ''
            for item in range(length2):
                password += random.choice(chars2)

            print(password)
            with open('user.txt', 'a') as x:
                x.write(uesr + password + '\n')
    if sa == "6":
        uesr = ''  
        chars2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'  
        amount = input('How many user')
        amount = int(amount)

        length2 = int(4)

        for password in range(amount):
            password = ''

            for item in range(length2):
                password = ''
            for item in range(length2):
                password += random.choice(chars2)

            print(password)
            with open('user.txt', 'a') as x:
                x.write(uesr + password + '\n')
    if sa == "7":
        uesr = ''  
        chars2 = 'qwertyuiopasdfghjklzxcvbnm'  
        amount = input('How many user')
        amount = int(amount)
        length2 = int(4)

        for password in range(amount):
            password = ''

            for item in range(length2):
                password = ''
            for item in range(length2):
                password += random.choice(chars2)

            print(password)
            with open('user.txt', 'a') as x:
                x.write(uesr + password + '\n')
    if sa == "8":
        uesr = ''  
        chars2 = 'qwertyuiopasdfghjklzxcvbnm1234567890._'  
        amount = input('How many user')
        amount = int(amount)

        length2 = input('User length')
        length2 = int(length2)

        for password in range(amount):
            password = ''

            for item in range(length2):
                password = ''
            for item in range(length2):
                password += random.choice(chars2)

            print(password)
            with open('user.txt', 'a') as x:
                x.write(uesr + password + '\n')

