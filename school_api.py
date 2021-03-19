import requests
from PyQt5 import QtWidgets
import secrets
import sqlite3
from typing import Tuple
import pandas as pd
import sys
import school_api_gui
import plotly.graph_objects as go


def render_map():
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(
        visible=False, resolution=110, scope="usa",
        showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Blue"
    )
    fig.update_layout(height=300, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


def display_data():
    app = QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = school_api_gui.Ui_MainWindow()
    sys.exit(app.exec_())


def save_excel_db(filename: str, conn):
    df = pd.read_excel(filename)
    df_subset = df[['area_title', 'occ_title', 'tot_emp', 'h_pct25', 'a_pct25', 'occ_code']]
    df_subset.to_sql(name='states', con=conn, if_exists='replace', index=False)


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)   # connect to existing DB or create new one
    cursor = db_connection.cursor()     # get ready to read/write data
    return db_connection, cursor


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute("DROP TABLE IF EXISTS schools")
    cursor.execute('''CREATE TABLE IF NOT EXISTS schools(
    school_id INTEGER PRIMARY KEY,
    school_name TEXT NOT NULL,
    school_state TEXT NOT NULL,
    school_city TEXT NOT NULL,
    student_size_2018 INTEGER,
    student_size_2017 INTEGER,
    three_year_earnings_over_poverty INTEGER,
    repayment_overall INTEGER,
    repayment_cohort INTEGER
    );''')
    # print('table created')


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def save_db(cursor, data):
    for school_data in data:
        cursor.execute(
            """INSERT INTO schools(school_id, school_name, school_state,
            school_city, student_size_2018, student_size_2017,
            three_year_earnings_over_poverty, repayment_overall, repayment_cohort) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (school_data['id'], school_data['school.name'], school_data['school.state'], school_data['school.city'],
             school_data['2018.student.size'], school_data['2017.student.size'],
             school_data['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line'],
             school_data['2016.repayment.3_yr_repayment.overall'],
             school_data['2016.repayment.repayment_cohort.3_year_declining_balance']))


def get_data():
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=" \
          "2,3&_fields=id,school.name,school.state,school.city,2018.student.size,2017.student.size,2017." \
          "earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall" \
          ",2016.repayment.repayment_cohort.3_year_declining_balance"
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
    # url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=" \
    #       "2,3&_fields=id,school.name,school.state,school.city,2018.student.size,2017.student.size,2017." \
    #       "earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall"
    # excel_file = "state_M2019_dl.xlsx"
    conn, cursor = open_db("school_db.sqlite")
    all_data = get_data()
    save_data(all_data)
    setup_db(cursor)
    save_db(cursor, all_data)
    # all_data.sort(key=get_key)
    # save_excel_db(excel_file, conn)
    # conn, cursor = open_db("state_db.sqlite")
    # display_data()
    close_db(conn)


if __name__ == '__main__':
    main()