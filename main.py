import requests, sqlite3
import sys
from typing import Tuple
from secrets import apiKey  # add a secrets file with wufoo_key='YoUr-WuFoo-KeY-Here'
from requests.auth import HTTPBasicAuth

# adjust this to your URL
url = "https://rkuczer.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"


def insert_db(cursor:sqlite3.Cursor):
   for entry in dataParse:
       cursor.execute('''      
       INSERT INTO entries (EntryId, first_name, last_name, job_title, company_name, phone_num, school_id)
    VALUES (:entryId, :first_name, :last_name, :job_title, :company_name, :phone_num, :school_id, :org_website,
        :course_proj, :guest_speaker, :site_visit, :job_shadow, :carreer_panel, :summer_2022, :fall_2022, :spring_2023, :summer_2023, :other, :yes_no)
        ''', entry["EntryId"], entry["Field1"], entry["Field2"], entry["Field426"], entry["Field428"], entry["Field10"],
        entry["Field12"])


def get_wufoo_data() -> dict:
    response = requests.get(url, auth=HTTPBasicAuth(apiKey, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse


def main():
    data = get_wufoo_data()
    data1 = data['Entries']
    file_to_save = open("info.txt", 'w')
    save_data(data1, save_file=file_to_save)

    conn, cursor = open_db("demo_db.sqlite")
    print(type(conn))
    setup_db(cursor)
    close_db(conn)

def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file=save_file)


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

if __name__ == '__main__':
    main()




















