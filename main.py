from secrets import apiKey
import requests, json, urllib3
import urllib.request

subdomain= 'rkuczer'
url = (f'https://{subdomain}.wufoo.com/api/v3/')
formHash= 'zqleboe1115c3h'
def getInfo():
    formHash = 'zqleboe1115c3h'
    global url
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, apiKey, formHash)
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    return opener

def getResponse(opener):
    global url
    response = opener.open(url + (f'forms/{formHash}/entries.json'))
    if response.status == 200:
        data = json.load(response)
        dataParse = (json.dumps(data, indent=4, separators=('', ':')))
    else:
        print(f'Error {response.status_code}: {response.text}')
        exit()
    print(dataParse)
    return dataParse

def saveFile(dataParse):
    formatData = ""
    for entry in dataParse:
        formatData += entry
    with open("info.txt", "w") as file:
        file.write(dataParse)
    file.close()
    #print(formatData)

opener = getInfo()
dataParse = getResponse(opener)
saveFile(dataParse)