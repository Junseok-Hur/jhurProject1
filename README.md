# jhurProject1
1. Junseok Hur


2. Any install and run directions I need beyond the basics.
- requests
- Confidential API Key (differs by users)
- sqlite3
- tuple
- openpyxl
- PyQt5
- sys
- pathlib


3. A brief description of what your project does
- API Data is received from the site using API Key and inserted as a text file.


4. a very brief discussion of your database layout and the table(s) you used
- I really invested a lot of time to solve this problem, but I was very disappointed that the parenthesis and one loop state were the problems to insert data into table.
- Using the API key value and the phrase "degrees_awarded.predominant=2,3", go to the tree with the desired value, take the value of the specified field, and insert it into the database. To insert data into the database, database is first created and connected. Then create a table and insert the specified value.


5. A  brief description of what is missing from the project (if anything)
*** Missing from the project***
- The second analysis should render a map to visualize the data.
- the data Analysis
allow the user to choose the following data fr either map or text visualization
compare the number of college graduates in a state (for the most recent year) with number of jobs in that state that likely expect a college education. (lets remove those that usually require a specialized school like police academies or apprenticeships). So lets remove all those professions which have an occ_code that begins with 30-39 or 40-49. (yes this is a broad brush, but we need to do this in 2 weeks)
comparing total jobs isn't going to be perfect since it isn't entry level jobs, but that data required a second API key
Compare the 3 year graduate cohort declining balance percentage to the 25% salary in the state and visualize that data
- Test is not done
