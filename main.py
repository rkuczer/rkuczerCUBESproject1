import requests, json, urllib3
import urllib.request
def createPassManager(password_mgr):
    username = '3ZZ4-X0EF-NFY1-6IYY'
    password = 'zqleboe1115c3h'
    url = 'https://rkuczer.wufoo.com/api/v3/'
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)
    return password_mgr
def createAuthHandler(password_mgr, url):
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    opener = urllib.request.build_opener(auth_handler)
    response = opener.open(url+'forms.json')

def printResponse(response):
    print(response.read())
    #response = requests.get(f"{url}forms/{password}/entries.json", params={"api_key": apiKey})


    #if response.status_code == 200:
    #    print(response.json())
    #else:
    #    print(f'Error {response.status_code}: {response.text}')



createPassManager()
createAuthHandler()
printResponse()