import requests
import secrets
import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)   # connect to existing DB or create new one
    cursor = db_connection.cursor()     # get ready to read/write data
    return db_connection, cursor


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS schools(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    state TEXT NOT NULL,
    city TEXT NOT NULL,
    '2018.student.size' INTEGER DEFAULT NULL,
    '2017.student.size' INTEGER DEFAULT NULL,
    '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line' INTEGER DEFAULT NULL,
    '2016.repayment.3_yr_repayment.overall' INTEGER DEFAULT NULL
    );''')
    print('table created')


def close_db(connection: sqlite3.Connection):
    connection.commit()     # make sure any changes get saved
    connection.close()


# def add_school(cursor: sqlite3.Cursor, id, name, state, city, STU_2018_N, STU_2017_N, CNTOVER150_3YR, RPY_3YR_N):
#     cursor.execute(f'''INSERT INTO STUDENTS (id, name, state, city, STU_2018_N, STU_2017_N, CNTOVER150_3YR, RPY_3YR_N)
#     VALUES({id}, {name}, {state}, {city}, {STU_2018_N}, {STU_2017_N}, {CNTOVER150_3YR}, {RPY_3YR_N})''')
#


def initial_schools(cursor: sqlite3.Cursor, data):
    cursor.executemany("INSERT INTO schools(id, name, state, city, '2018.student.size', '2017.student.size', "
                       "'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line', "
                       "'2016.repayment.3_yr_repayment.overall') VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)


def check_table(cursor: sqlite3.Cursor):
    for row in cursor.fetchall():
        print(row)


def get_data(url: str):
    final_data = []
    entire_data = True
    page = 0
    while entire_data:
        final_url = f"{url}&api_key={secrets.api_key}&page={page}"
        response = requests.get(final_url)
        if response.status_code != 200:
            print(response.text)
            return []
        json_data = response.json()
        page_data = json_data["results"]
        # initial_schools(cursor, page_data)
        final_data.extend(page_data)
        if len(page_data) < 20:
            entire_data = False
        page += 1

    return final_data


def save_data(data, filename='SchoolData.txt'):
    with open(filename, 'w') as file:
        for item in data:
            print(item, file=file)
        file.close()


def main():
    # comment to test workflow
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=" \
          "2,3&fields=id,2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_" \
          "count_over_poverty_line,2017.student.size,2018.student.size,school.city,school.state,school.name"
    conn, cursor = open_db("school_db.sqlite")
    all_data = get_data(url)
    save_data(all_data)
    dataframe = list()
    dataframe.append(all_data)
    # for school_data in all_data:
    #    print(school_data)
    setup_db(cursor)
    initial_schools(cursor, dataframe)
    # check_table(cursor)
    close_db(conn)


if __name__ == '__main__':
    main()
