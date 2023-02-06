from main import get_wufoo_data, open_db, setup_db, close_db, insert_db


def test_data_num():
    response = get_wufoo_data()
    data1 = response['Entries']
    assert len(data1) == 10, f"Expected 10 entries, but got {len(data1)}"
    return data1


def test_db():
    conn, cursor = open_db("test_db.sqlite")

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