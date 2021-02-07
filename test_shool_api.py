import pytest
import school_api

#
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 187, '2017.student.size': 1007,
#  'school.name': 'Kauai Community College', '2018.student.size': 929, 'school.state': 'HI', 'id': 141802,
#  'school.city': 'Lihue', '2016.repayment.3_yr_repayment.overall': 273}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 437, '2017.student.size': 6660,
#  'school.name': 'City Colleges of Chicago-Wilbur Wright College', '2018.student.size': 6257, 'school.state': 'IL',
#  'id': 144218, 'school.city': 'Chicago', '2016.repayment.3_yr_repayment.overall': 412}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 125, '2017.student.size': 274,
#  'school.name': 'Midstate College', '2018.student.size': 224, 'school.state': 'IL', 'id': 147165,
#  'school.city': 'Peoria', '2016.repayment.3_yr_repayment.overall': 492}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 697, '2017.student.size': 11104,
#  'school.name': 'Moraine Valley Community College', '2018.student.size': 10219, 'school.state': 'IL', 'id': 147378,
#  'school.city': 'Palos Hills', '2016.repayment.3_yr_repayment.overall': 1358}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 662, '2017.student.size': 6875,
#  'school.name': 'Illinois Central College', '2018.student.size': 6397, 'school.state': 'IL', 'id': 145682,
#  'school.city': 'East Peoria', '2016.repayment.3_yr_repayment.overall': 2311}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 182, '2017.student.size': 3049,
#  'school.name': 'John A Logan College', '2018.student.size': 3035, 'school.state': 'IL', 'id': 146205,
#  'school.city': 'Carterville', '2016.repayment.3_yr_repayment.overall': 268}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 277, '2017.student.size': 1519,
#  'school.name': 'John Wood Community College', '2018.student.size': 1555, 'school.state': 'IL', 'id': 146278,
#  'school.city': 'Quincy', '2016.repayment.3_yr_repayment.overall': 1019}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 285, '2017.student.size': 2518,
#  'school.name': 'Kishwaukee College', '2018.student.size': 2295, 'school.state': 'IL', 'id': 146418,
#  'school.city': 'Malta', '2016.repayment.3_yr_repayment.overall': 1444}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 583, '2017.student.size': 4530,
#  'school.name': 'Lincoln Land Community College', '2018.student.size': 4414, 'school.state': 'IL', 'id': 146685,
#  'school.city': 'Springfield', '2016.repayment.3_yr_repayment.overall': 1612}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 42, '2017.student.size': 101,
#  'school.name': 'Mid-America College of Funeral Service', '2018.student.size': 122, 'school.state': 'IN',
#  'id': 151962, 'school.city': 'Jeffersonville', '2016.repayment.3_yr_repayment.overall': 118}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 92, '2017.student.size': 1475,
#  'school.name': 'Allen County Community College', '2018.student.size': 1432, 'school.state': 'KS', 'id': 154642,
#  'school.city': 'Iola', '2016.repayment.3_yr_repayment.overall': 1220}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 138, '2017.student.size': 1019,
#  'school.name': 'Marshalltown Community College', '2018.student.size': 927, 'school.state': 'IA', 'id': 153922,
#  'school.city': 'Marshalltown', '2016.repayment.3_yr_repayment.overall': 1103}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 257, '2017.student.size': 2001,
#  'school.name': 'Cowley County Community College', '2018.student.size': 1958, 'school.state': 'KS', 'id': 154952,
#  'school.city': 'Arkansas City', '2016.repayment.3_yr_repayment.overall': 2619}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 90, '2017.student.size': 1103,
#  'school.name': 'Dodge City Community College', '2018.student.size': 965, 'school.state': 'KS', 'id': 154998,
#  'school.city': 'Dodge City', '2016.repayment.3_yr_repayment.overall': 330}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 115, '2017.student.size': 274,
#  'school.name': "St Luke's College", '2018.student.size': 271, 'school.state': 'IA', 'id': 154262,
#  'school.city': 'Sioux City', '2016.repayment.3_yr_repayment.overall': 130}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 359, '2017.student.size': 1676,
#  'school.name': 'Southeastern Community College', '2018.student.size': 1608, 'school.state': 'IA', 'id': 154378,
#  'school.city': 'West Burlington', '2016.repayment.3_yr_repayment.overall': 1534}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 544, '2017.student.size': 3739,
#  'school.name': 'Hutchinson Community College', '2018.student.size': 3442, 'school.state': 'KS', 'id': 155195,
#  'school.city': 'Hutchinson', '2016.repayment.3_yr_repayment.overall': 2074}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 238, '2017.student.size': 2945,
#  'school.name': 'South Suburban College', '2018.student.size': 2821, 'school.state': 'IL', 'id': 149365,
#  'school.city': 'South Holland', '2016.repayment.3_yr_repayment.overall': None}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 402, '2017.student.size': 8073,
#  'school.name': 'Triton College', '2018.student.size': 8029, 'school.state': 'IL', 'id': 149532,
#  'school.city': 'River Grove', '2016.repayment.3_yr_repayment.overall': 829}
# {'2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 46, '2017.student.size': 510,
#  'school.name': 'Ancilla College', '2018.student.size': 369, 'school.state': 'IN', 'id': 150048,
#  'school.city': 'Donaldson', '2016.repayment.3_yr_repayment.overall': 478}
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,2016.repayment.3_yr_repayment.overall,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2017.student.size,2018.student.size,school.city,school.state,school.name"

@pytest.fixture()
def test_get_data():
    return school_api.get_data(url)

def test_save_data():
    mock_data = {"'school.name': 'Mock School', '2018.student.size': 200"}
    list_data = []
    list_data.append(mock_data)
    file_name = "mock.txt"
    school_api.save_data(list_data, file_name)
    test_file = open(file_name, 'r')
    saved_data = test_file.readlines()
    assert f"{str(mock_data)}\n" in saved_data









