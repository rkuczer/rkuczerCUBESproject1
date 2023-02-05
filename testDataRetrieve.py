import pytest
import sqlite3
from typing import Tuple
from main import get_wufoo_data, open_db, setup_db, close_db, insert_db


def test_data_num():
    response = get_wufoo_data()
    data1 = response['Entries']
    assert len(data1) == 10, f"Expected 10 entries, but got {len(data1)}"
    return data1

def test_db():
    conn, cursor = open_db("test_db.sqlite")
    #not using testEntry here
    testEntry = {'EntryId': '1', 'Field1': 'James', 'Field2': 'Pellerin', 'Field426': 'Cyber Analyst', 'Field428': 'MITRE',
                 'Field10': '5085555555', 'Field12': '394356', 'Field430': 'mitre.com', 'Field123': '', 'Field124': '', 'Field125': '', 'Field126': ' Job Shadow', 'Field127': '',
                'Field223': 'Summer 2022 (June 2022- August 2022)', 'Field224': '', 'Field225': '', 'Field226': '',
                'Field227': '', 'Field423': 'Yes', 'DateCreated': '2023-01-19 21:32:01', 'CreatedBy': 'public',
                'DateUpdated': '', 'UpdatedBy': None}


    print(type(conn))
    response = get_wufoo_data()
    data1 = response['Entries']
    setup_db(cursor)
    insert_db(cursor, data1)

    cursor.execute("SELECT * FROM entries LIMIT 1")
    result = cursor.fetchone()
    assert result is not None, "No entry found in the first row of the table"
    close_db(conn)



if __name__ == '__main__':
   test_data_num()