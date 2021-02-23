import requests
import secrets
import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename, isolation_level=None)   # connect to existing DB or create new one
    cursor = db_connection.cursor()     # get ready to read/write data
    return db_connection, cursor


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS schools(
    school_id INTEGER PRIMARY KEY,
    school_name TEXT NOT NULL,
    school_state TEXT NOT NULL,
    school_city TEXT NOT NULL,
    student_size_2018 INTEGER,
    student_size_2017 INTEGER,
    three_year_earnings_over_poverty INTEGER,
    repayment_overall INTEGER
    );''')
    print('table created')


def close_db(connection: sqlite3.Connection):
    connection.commit()     # make sure any changes get saved
    connection.close()


def save_db(cursor, data):
    for school_data in data:
        cursor.execute(
            """INSERT INTO schools(school_id, school_name, school_state, school_city, student_size_2018, 
            student_size_2017, three_year_earnings_over_poverty, repayment_overall) VALUES(?,   ?, ?, ?, ?, ?, ?, ?)""",
            (school_data['id'], school_data['school.name'], school_data['school.state'], school_data['school.city'],
             school_data['2018.student.size'], school_data['2017.student.size'],
             school_data['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line'],
             school_data['2016.repayment.3_yr_repayment.overall']))


# def check_table(cursor: sqlite3.Cursor):
#     for row in cursor.fetchall():
#         print(row)


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
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=" \
          "2,3&_fields=id,school.name,school.state,school.city,2018.student.size,2017.student.size,2017." \
          "earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall"
    conn, cursor = open_db("school_db.sqlite")
    all_data = get_data(url)
    save_data(all_data)
    setup_db(cursor)
    save_db(cursor, all_data)
    close_db(conn)
    # print(all_data)


if __name__ == '__main__':
    main()
