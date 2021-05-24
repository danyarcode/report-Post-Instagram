import os
import sys
import requests
import time
import re
import urllib.parse
os.system('clear')
ani =('''\033[1;33m
                          ________________________________
                  ________|                               |_______
                  \       |         HAMA SOFTWARE         |      /
                   \      |      Report Post Instagram    |     / 
                   /      |_______________________________|     \ 
                  /__________)                         (_________\ \
                  \033[1;37m
                  ''')
                  
def banner():#hama_software
        print ('''\033[1;33m
                          ________________________________
                  ________|                               |_______
                  \       |         HAMA SOFTWARE         |      /
                   \      |      Report Post Instagram    |     / 
                   /      |_______________________________|     \ 
                  /__________)                         (_________\ \
                  \033[1;37m
                  ''')

loop = True
if loop:
   url = "https://textuploader.com/tsmes/raw"
   gets = requests.get(url).text
   if "BYE" in gets:
     print("This Tool Stopped By @hama_software Sorry Bro :( ")
     sys.exit()
   else:
     loop = False
banner()

U = input("[?] Username:")
P = input("[?] Password:")
def spam_p():
  dyar = 0
  print("----------------------")
  POST_CODE = input("[ POST_CODE ] : ")
  print("----------------------")
  POST_URL = "https://www.instagram.com/p/"+POST_CODE+"/"
  URL_GET = "https://www.instagram.com/p/"+POST_CODE+"/?__a=1"
  GET_U = requests.get(URL_GET, headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Host":"www.instagram.com"}).text
  find = re.compile(r'"id":"(.*?)"')
  find_id = find.findall(GET_U)
  POST_ID = find_id[0]


  #----------$-------------$---&-&&
  HEAD = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '274',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
  }
  URL = 'https://www.instagram.com/accounts/login/ajax/'
  PAYLOAD = {
    'username': U,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+P,
    'queryParams': '{}',
    'optIntoOneTap': 'false'
  }
  LOGIN = requests.post(URL, headers=HEAD, data=PAYLOAD)
  if '{"user":false,' in LOGIN.text:
    print("Email Or Password is Wrong ( "+U+" )")
    exit()
  elif '{"user":true,' in LOGIN.text:
    print("Login As ( "+U+" )")
    login = True
  login_ses = LOGIN.cookies
  #---------------------------
  URL_C = "https://www.instagram.com/reports/web/get_frx_prompt/"
  HEAD_C = {
     "Host":"www.instagram.com",
     "user-agent":"Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0",
     "accept":"*/*",
     "accept-language":"en-US",
     "x-csrftoken":login_ses['csrftoken'],
     "x-instagram-ajax":"c795b4273c42",
     "x-ig-app-id":"1217981644879628",
     "x-ig-www-claim":"hmac.AR1ByrQc_I8HfEoz9O_X33VqtGFqzMIie7L3xZh1VhGQ8r0n",
     "content-type":"application/x-www-form-urlencoded",
     "x-requested-with":"XMLHttpRequest",
     "origin":"https://www.instagram.com",
     "referer":POST_URL
  }
  DATA_C = {
    "entry_point":"1",
    "location":"6",
    "object_type":"1",
    "object_id":POST_ID,
    "container_module":"postPage",
    "frx_prompt_request_type":"1"
  }
  GET_CONTEXT = requests.post(URL_C, headers=HEAD_C, data=DATA_C, cookies=login_ses)
  GET_TEXT = GET_CONTEXT.json()['response']['context']
  ENCODE_CONTEXT = urllib.parse.quote(GET_TEXT)
  API_V = "ig_spam_v3"
  for i in range(999999):
    URS = "https://www.instagram.com/reports/web/log_tag_selected/"
    HEAD_rep = {"Host":"www.instagram.com","user-agent":"Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0","accept":"*/*","x-csrftoken":login_ses['csrftoken'],"x-instagram-ajax":"c795b4273c42","x-ig-app-id":"1217981644879628","x-ig-www-claim":"hmac.AR1ByrQc_I8HfEoz9O_X33VqtGFqzMIie7L3xZh1VhGQ8r0n","content-type":"application/x-www-form-urlencoded","x-requested-with":"XMLHttpRequest","origin":"https://www.instagram.com","referer":POST_URL}
    DATA_rep = {"context":ENCODE_CONTEXT,"selected_tag_type":API_V}
    SEND_R = requests.post(URS, headers=HEAD_rep, data=DATA_rep, cookies=login_ses)
    F = SEND_R.json()['status']
    os.system("clear")
    print(ani)
    print("\n\nAccount Instagram (@{})".format(U))
    print("\n[REPORT ] SEND REPORT : "+str(dyar))
    dyar+= 1
    time.sleep(2)

def self_p():
  dyar2=0
  print("----------------------")
  POST_CODE = input("[ POST_CODE ] : ")
  print("----------------------")
  POST_URL = "https://www.instagram.com/p/"+POST_CODE+"/"
  URL_GET = "https://www.instagram.com/p/"+POST_CODE+"/?__a=1"
  GET_U = requests.get(URL_GET, headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Host":"www.instagram.com"}).text
  find = re.compile(r'"id":"(.*?)"')
  find_id = find.findall(GET_U)
  POST_ID = find_id[0]


  #----------$-------------$---&-&&
  HEAD = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '274',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
  }
  URL = 'https://www.instagram.com/accounts/login/ajax/'
  PAYLOAD = {
    'username': U,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+P,
    'queryParams': '{}',
    'optIntoOneTap': 'false'
  }
  LOGIN = requests.post(URL, headers=HEAD, data=PAYLOAD)
  if '{"user":false,' in LOGIN.text:
    print("Email Or Password is Wrong ( "+U+" )")
    exit()
  elif '{"user":true,' in LOGIN.text:
    print("Login As ( "+U+" )")
    login = True
  login_ses = LOGIN.cookies
  #---------------------------
  URL_C = "https://www.instagram.com/reports/web/get_frx_prompt/"
  HEAD_C = {
     "Host":"www.instagram.com",
     "user-agent":"Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0",
     "accept":"*/*",
     "accept-language":"en-US",
     "x-csrftoken":login_ses['csrftoken'],
     "x-instagram-ajax":"c795b4273c42",
     "x-ig-app-id":"1217981644879628",
     "x-ig-www-claim":"hmac.AR1ByrQc_I8HfEoz9O_X33VqtGFqzMIie7L3xZh1VhGQ8r0n",
     "content-type":"application/x-www-form-urlencoded",
     "x-requested-with":"XMLHttpRequest",
     "origin":"https://www.instagram.com",
     "referer":POST_URL
  }
  DATA_C = {
    "entry_point":"1",
    "location":"6",
    "object_type":"1",
    "object_id":POST_ID,
    "container_module":"postPage",
    "frx_prompt_request_type":"1"
  }
  GET_CONTEXT = requests.post(URL_C, headers=HEAD_C, data=DATA_C, cookies=login_ses)
  GET_TEXT = GET_CONTEXT.json()['response']['context']
  ENCODE_CONTEXT = urllib.parse.quote(GET_TEXT)
  API_V = "ig_self_injury_v3"
  for i in range(999999):
    URS = "https://www.instagram.com/reports/web/log_tag_selected/"
    HEAD_rep = {"Host":"www.instagram.com","user-agent":"Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0","accept":"*/*","x-csrftoken":login_ses['csrftoken'],"x-instagram-ajax":"c795b4273c42","x-ig-app-id":"1217981644879628","x-ig-www-claim":"hmac.AR1ByrQc_I8HfEoz9O_X33VqtGFqzMIie7L3xZh1VhGQ8r0n","content-type":"application/x-www-form-urlencoded","x-requested-with":"XMLHttpRequest","origin":"https://www.instagram.com","referer":POST_URL}
    DATA_rep = {"context":ENCODE_CONTEXT,"selected_tag_type":API_V}
    SEND_R = requests.post(URS, headers=HEAD_rep, data=DATA_rep, cookies=login_ses)
    F = SEND_R.json()['status']
    os.system("clear")
    print(ani)
    print("\n\nAccount Instagram (@{})".format(U))
    print("\n[REPORT ] SEND REPORT : "+str(dyar2))
    dyar2+= 1

def hate_p():
  dyar22 = 0
  print("----------------------")
  POST_CODE = input("[ POST_CODE ] : ")
  print("----------------------")
  POST_URL = "https://www.instagram.com/p/"+POST_CODE+"/"
  URL_GET = "https://www.instagram.com/p/"+POST_CODE+"/?__a=1"
  GET_U = requests.get(URL_GET, headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Host":"www.instagram.com"}).text
  find = re.compile(r'"id":"(.*?)"')
  find_id = find.findall(GET_U)
  POST_ID = find_id[0]


  #----------$-------------$---&-&&
  HEAD = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '274',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
  }
  URL = 'https://www.instagram.com/accounts/login/ajax/'
  PAYLOAD = {
    'username': U,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+P,
    'queryParams': '{}',
    'optIntoOneTap': 'false'
  }
  LOGIN = requests.post(URL, headers=HEAD, data=PAYLOAD)
  if '{"user":false,' in LOGIN.text:
    print("Email Or Password is Wrong ( "+U+" )")
    exit()
  elif '{"user":true,' in LOGIN.text:
    print("Login As ( "+U+" )")
    login = True
  login_ses = LOGIN.cookies
  #---------------------------
  URL_C = "https://www.instagram.com/reports/web/get_frx_prompt/"
  HEAD_C = {
     "Host":"www.instagram.com",
     "user-agent":"Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0",
     "accept":"*/*",
     "accept-language":"en-US",
     "x-csrftoken":login_ses['csrftoken'],
     "x-instagram-ajax":"c795b4273c42",
     "x-ig-app-id":"1217981644879628",
     "x-ig-www-claim":"hmac.AR1ByrQc_I8HfEoz9O_X33VqtGFqzMIie7L3xZh1VhGQ8r0n",
     "content-type":"application/x-www-form-urlencoded",
     "x-requested-with":"XMLHttpRequest",
     "origin":"https://www.instagram.com",
     "referer":POST_URL
  }
  DATA_C = {
    "entry_point":"1",
    "location":"6",
    "object_type":"1",
    "object_id":POST_ID,
    "container_module":"postPage",
    "frx_prompt_request_type":"1"
  }
  GET_CONTEXT = requests.post(URL_C, headers=HEAD_C, data=DATA_C, cookies=login_ses)
  GET_TEXT = GET_CONTEXT.json()['response']['context']
  ENCODE_CONTEXT = urllib.parse.quote(GET_TEXT)
  API_V = "ig_hate_speech_v3"
  for i in range(999999):
    URS = "https://www.instagram.com/reports/web/log_tag_selected/"
    HEAD_rep = {"Host":"www.instagram.com","user-agent":"Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0","accept":"*/*","x-csrftoken":login_ses['csrftoken'],"x-instagram-ajax":"c795b4273c42","x-ig-app-id":"1217981644879628","x-ig-www-claim":"hmac.AR1ByrQc_I8HfEoz9O_X33VqtGFqzMIie7L3xZh1VhGQ8r0n","content-type":"application/x-www-form-urlencoded","x-requested-with":"XMLHttpRequest","origin":"https://www.instagram.com","referer":POST_URL}
    DATA_rep = {"context":ENCODE_CONTEXT,"selected_tag_type":API_V}
    SEND_R = requests.post(URS, headers=HEAD_rep, data=DATA_rep, cookies=login_ses)
    F = SEND_R.json()['status']
    os.system("clear")
    print(ani)
    print("\n\nAccount Instagram (@{})".format(U))
    print("\n[REPORT ] SEND REPORT : "+str(dyar22))
    dyar22+= 1
   
    time.sleep(2)

def main():
  print("\x1b[36;1m")
  print("\x1b[37;1m")
  print("Report Post V1 By hama_software\n")
  print("[ 1 ] Self (Post)")
  print("[ 2 ] Hate & Speach (Post)")
  print("[ 3 ] Spam (Post)")
  print("----------------------")
  x = input("[ OPTION ] : ")
  if x=="1":
    os.system("clear")
    self_p()
  elif x=="2":
    os.system("clear")
    hate_p()
  elif x=="3":
    os.system("clear")
    spam_p()
main()