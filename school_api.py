import requests
import secrets

def get_data(url: str):
    final_data = []
    entire_data = True
    page = 0
    while entire_data:
        final_url = f"{url}&api_key={secrets.api_key}&page={page}"
        # final_url = f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size,2018.student.size,school.city,school.state,school.name&api_key={secrets.api_key}&page={page}"
        response = requests.get(final_url)
        # response = requests.get(url)
        if response.status_code != 200:
            print(response.text)
            return []
        json_data = response.json()
        page_data = json_data["results"]
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
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size,2018.student.size,school.city,school.state,school.name"
    # url = f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size,2018.student.size,school.city,school.state,school.name&api_key={secrets.api_key}&page={page}"

    all_data = get_data(url)
    for school_data in all_data:
        print(school_data)
    save_data(all_data)


if __name__ == '__main__':
    main()