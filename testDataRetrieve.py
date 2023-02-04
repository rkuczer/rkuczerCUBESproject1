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
        cursor.execute('''CREATE TABLE IF NOT EXISTS testEntries(
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


    def test_db(self):
        conn, cursor = open_db("test_db.sqlite")
        #changed this to a dict
        testEntry = [('EntryId', '1'), ('Field1', 'James '), ('Field2', 'Pellerin'), ('Field426', 'Cyber Analyst'), ('Field428', 'MITRE'),
                     ('Field10', '5085555555'), ('Field12', '394356'), ('Field430', 'mitre.com'), ('Field123', ''), ('Field124', ''),
                     ('Field125', ''), ('Field126', ' Job Shadow'), ('Field127', ''),
                     ('Field223', 'Summer 2022 (June 2022- August 2022)'), ('Field224', ''), ('Field225', ''), ('Field226', ''),
                     ('Field227', ''), ('Field423', 'Yes'), ('DateCreated', '2023-01-19 21:32:01'), ('CreatedBy', 'public'),
                     ('DateUpdated', ''), ('UpdatedBy', None)]


        print(type(conn))
        setup_db(cursor)

        #insert_db(cursor, dictTest)

        cursor.execute('SELECT * FROM testEntries WHERE EntryId=? AND first_name=?', ('1', 'James'))

        result = cursor.fetchone()
        self.assertEqual(result, ('1', 'James'))
        close_db(conn)



if __name__ == '__main__':
    unittest.main()