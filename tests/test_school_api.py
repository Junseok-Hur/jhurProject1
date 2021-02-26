import school_api as sa



def test_get_data():
    data = sa.get_data()
    assert len(data) > 3000


def test_save_db():
    # first lets add test data
    conn, cursor = sa.open_db('testdb.sqlite')
    sa.setup_db(cursor)
    test_data = [{'school.name': 'Test University', '2018.student.size': 1000, '2017.student.size': 800,
                  'school.state': 'MA', 'id': 11001, 'school.city': 'Brockton',
                  '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 456,
                  '2016.repayment.3_yr_repayment.overall': 4004}]
    sa.save_db(cursor, test_data)
    sa.close_db(conn)
    # test data is saved - now lets see if it is there
    conn, cursor = sa.open_db('testdb.sqlite')
    # the sqlite_master table is a metadata table with information about all the tables in it
    cursor.execute('''SELECT name FROM sqlite_master
    WHERE type ='table' AND name LIKE 'school_%';''')  # like does pattern matching with % as the wildcard
    results = cursor.fetchall()
    assert len(results) == 1
    cursor.execute(''' SELECT school_name FROM schools''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Test University'


def test_read_xlsx_properly():
    excel_file = "./state_M2019_dl.xlsx"
    conn, cursor = sa.open_db("testdb.sqlite")
    df = sa.pd.read_excel(excel_file)
    df.to_sql(name='test_states', con=conn, if_exists='append', index=False)
    cursor.execute('''SELECT test_states.area_title as "State_Name" FROM test_states WHERE test_states.area_type = "2"
    and test_states.area_title is not "District of Columbia" GROUP BY test_states.area_title''')
    results = cursor.fetchall()
    test_record = len(results)
    assert test_record == 50


def test_save_excel_db():
    pass


def test_table_exist():
    pass


def test_new_table_work():
    pass
