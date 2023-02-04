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

    def test_db(self):
        conn, cursor = open_db("test_db.sqlite")
        #changed this to a dict
        testEntry = {'EntryId': '1', 'Field1': 'James', 'Field2': 'Pellerin', 'Field426': 'Cyber Analyst', 'Field428': 'MITRE',
                     'Field10': '5085555555', 'Field12': '394356', 'Field430': 'mitre.com', 'Field123': '', 'Field124': '',
                     'Field125': '', 'Field126': ' Job Shadow', 'Field127': '',
                     'Field223': 'Summer 2022 (June 2022- August 2022)', 'Field224': '', 'Field225': '', 'Field226': '',
                     'Field227': '', 'Field423': 'Yes', 'DateCreated': '2023-01-19 21:32:01', 'CreatedBy': 'public',
                     'DateUpdated': '', 'UpdatedBy': None}


        print(type(conn))
        setup_db(cursor)
        data = get_wufoo_data()
        data1 = data['Entries']
        insert_db(cursor, data1)

        cursor.execute('SELECT * FROM entries WHERE EntryId=? AND first_name=?', ('1', 'James'))

        result = cursor.fetchone()
        self.assertEqual((1, 'James'), result)
        close_db(conn)



if __name__ == '__main__':
    unittest.main()