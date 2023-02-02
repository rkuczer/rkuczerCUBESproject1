from secrets import apiKey
from typing import Tuple
import json
import urllib.request
import sqlite3


subdomain = 'rkuczer'
url = (f'https://{subdomain}.wufoo.com/api/v3/')
formHash = 'zqleboe1115c3h'


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


def open_db(filename:str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)#connect to existing DB or create new one
    cursor = db_connection.cursor()#get ready to read/write data
    return db_connection, cursor


def close_db(connection:sqlite3.Connection):
    connection.commit()#make sure any changes get saved
    connection.close()


def setup_db(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries(
 EntryId INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
 job_title TEXT NOT NULL, company_name TEXT NOT NULL, phone_num INTEGER NOT NULL, 
 school_id INTEGER NOT NULL);''')


def insert_db(cursor:sqlite3.Cursor, dataParse):
    for entry in dataParse:
        cursor.execute('''
        INSERT INTO entries (EntryId, first_name, last_name, job_title, company_name, phone_num, school_id)
        VALUES (:entryId, :first_name, :last_name, :job_title, :company_name, :phone_num, :school_id, :org_website,
        :course_proj, :guest_speaker, :site_visit, :job_shadow, :carreer_panel, :summer_2022, :fall_2022, :spring_2023, :summer_2023, :other, :yes_no)
        ''', entry["EntryId"], entry["Field1"], entry["Field2"], entry["Field426"], entry["Field428"], entry["Field10"],
        entry["Field12"])





def main():
    opener = getInfo()
    dataParse = getResponse(opener)
    saveFile(dataParse)
    conn, cursor = open_db("demo_db.sqlite")
    print(type(conn))
    setup_db(cursor)
    insert_db(cursor, dataParse)
    close_db(conn)


if __name__ == '__main__':
    main()








