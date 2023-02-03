import requests
import sqlite3
import sys
from typing import Tuple
from secrets import apiKey
from requests.auth import HTTPBasicAuth


url = "https://rkuczer.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"


def insert_db(cursor: sqlite3.Cursor, data1):
    for key in data1:
        EntryId = key['EntryId']
        first_name = key['Field1']
        last_name = key['Field2']
        job_title = key['Field426']
        org_name = key['Field428']
        phone_num = key['Field10']
        school_id = key['Field12']
        org_site = key['Field430']
        course = key['Field123']
        speaker = key['Field124']
        siteVisit = key['Field125']
        job_shadow = key['Field126']
        carreer_panel = key['Field127']
        summer_2022 = key['Field223']
        fall_2022 = key['Field224']
        spring_2023 = key['Field225']
        summer_2023 = key['Field226']
        other = key['Field227']
        permission = key['Field423']
        date_created = key['DateCreated']
        created_by = key['CreatedBy']
        date_update = key['DateUpdated']
        updated_by = key['UpdatedBy']
        try:
            cursor.execute("INSERT INTO entries (EntryId, first_name, last_name, job_title, org_name, phone_num, "
                           "school_id, org_site, course, speaker, siteVisit, job_shadow, carreer_panel, summer_2022, fall_2022, "
                           "spring_2023, summer_2023, "
                           "other, permission, date_created, created_by, date_update, updated_by) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (EntryId, first_name, last_name, job_title, org_name, phone_num, school_id, org_site, course, speaker, siteVisit, job_shadow,
                            carreer_panel, summer_2022, fall_2022, spring_2023, summer_2023, other, permission, date_created, created_by, date_update, updated_by))
        except sqlite3.IntegrityError:
            print(f"Form submission with entryID={EntryId} and submission_date={date_created} already exists, not adding this entry.")


def get_wufoo_data() -> dict:

    response = requests.get(url, auth=HTTPBasicAuth(apiKey, 'pass'))
    if response.status_code != 200:
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
    insert_db(cursor, data1)
    close_db(conn)


def save_data(data_to_save: list, save_file = None):

    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file = save_file)
        print("+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
              file = save_file)


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:

    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection:sqlite3.Connection):

    connection.commit()
    connection.close()


def setup_db(cursor:sqlite3.Cursor):

   cursor.execute('''CREATE TABLE IF NOT EXISTS entries(
 EntryId INTEGER UNIQUE NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
 job_title TEXT NOT NULL, org_name TEXT NOT NULL, phone_num INTEGER NOT NULL,
 school_id INTEGER NOT NULL, org_site TEXT, course TEXT, speaker TEXT, siteVisit TEXT, job_shadow TEXT, 
 carreer_panel TEXT, summer_2022 TEXT, fall_2022 TEXT, spring_2023 TEXT, summer_2023 TEXT, other TEXT, permission TEXT, date_created TEXT,
 created_by TEXT, date_update TEXT, updated_by TEXT);''')


if __name__ == '__main__':

    main()