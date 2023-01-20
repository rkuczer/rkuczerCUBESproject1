import requests, json, urllib3

def main():

    apiKey = '3ZZ4-X0EF-NFY1-6IYY'
    password = 'zqleboe1115c3h'

    url = 'https://rkuczer.wufoo.com/api/v3/'

    response = requests.get(f"{url}forms/{password}/entries.json", params={"api_key": apiKey})


    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Error {response.status_code}: {response.text}')



main()