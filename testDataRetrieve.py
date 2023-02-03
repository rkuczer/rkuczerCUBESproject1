import unittest
import sqlite3
from typing import Tuple
from main import get_wufoo_data, open_db, setup_db, close_db, insert_db

class MyTestCase(unittest.TestCase):
    def test_data_num(self):
        response = get_wufoo_data()
        data1 = response['Entries']
        self.assertEqual(10,len(data1))
        return data1

    def setup_db(cursor: sqlite3.Cursor):
        cursor.execute('''CREATE TABLE IF NOT EXISTS entries(
        EntryId INTEGER UNIQUE NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
        job_title TEXT NOT NULL, org_name TEXT NOT NULL, phone_num INTEGER NOT NULL,
        school_id INTEGER NOT NULL, org_site TEXT, course TEXT, speaker TEXT, siteVisit TEXT,
        job_shadow TEXT,
        carreer_panel TEXT, summer_2022 TEXT, fall_2022 TEXT, spring_2023 TEXT, summer_2023 TEXT, other TEXT,
        permission TEXT, date_created TEXT,
        created_by TEXT, date_update TEXT, updated_by TEXT);''')


    def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)
        cursor = db_connection.cursor()
        return db_connection, cursor


    def close_db(connection: sqlite3.Connection):
        connection.commit()
        connection.close()


    def test_db(self, data1):
        conn, cursor = open_db("test_db.sqlite")
        print(type(conn))
        setup_db(cursor)
        insert_db(cursor, data1)
        close_db(conn)



if __name__ == '__main__':
    unittest.main()