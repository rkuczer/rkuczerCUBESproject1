import requests, json, urllib3
import urllib.request

def getInfo():
    username = '3ZZ4-X0EF-NFY1-6IYY'
    password = 'zqleboe1115c3h'
    url = 'https://rkuczer.wufoo.com/api/v3/'

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)

    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)


    response = opener.open(url + 'forms/zqleboe1115c3h.json')
    data = json.load(response)

    dataParse = (json.dumps(data, indent=4, sort_keys=True))
    return dataParse

def saveFile(dataParse):
    with open("info.txt", "w") as file:
        file.write(dataParse)
    file.close()
    print(dataParse)

#print(response.read())
#def createPassManager(password_mgr):
#    username = '3ZZ4-X0EF-NFY1-6IYY'
#    password = 'zqleboe1115c3h'
#    url = 'https://rkuczer.wufoo.com/api/v3/'
#    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#    password_mgr.add_password(None, url, username, password)
#    return password_mgr
#def createAuthHandler(password_mgr, url):
#    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
 #   opener = urllib.request.build_opener(auth_handler)
 #   response = opener.open(url+'forms.json')

#def printResponse(response):
#    print(response.read())
    #response = requests.get(f"{url}forms/{password}/entries.json", params={"api_key": apiKey})


    #if response.status_code == 200:
    #    print(response.json())
    #else:
    #    print(f'Error {response.status_code}: {response.text}')


dataParse = getInfo()
saveFile(dataParse)