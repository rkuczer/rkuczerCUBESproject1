Ryan Kuczer
COMP 490

Imports: From requests.auth import HTTPBasicAuth, import sys, and requests

An API key is to be imported, a subdomain and form hash variables are needed to be changed to your own form's in the main.py file, the api key is not committed to the project on github.

The project gets info from my wufoo form and saves it to a sqllite table that is a part of a database.
There is two tests implemented the first checks if the correct number of data entries are returned from the wufoo api.
The second checks the database and table creation functions in main.py as well as the function that inserts the data into
the database, currently the test function only works if there are multiple entries being entered into the database but still correctly
checks for a test entry.

Currently, the database layout is a single table named 'entries' with each field in the json response as its own column. 

Currently, no missing components are in Sprint 1 Project 2.

Wufoo form location: https://rkuczer.wufoo.com/forms/zqleboe1115c3h/

