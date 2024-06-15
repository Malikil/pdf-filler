Installation
===

1. Make sure python 3.12 is installed. To verify, type `python --version` in command prompt
    1. To install python, go to [python.org](https://www.python.org) and download python 3.12 or newer
    2. When installing, make sure to check the option for 'Add python to PATH'
2. Make sure pipenv is installed. To verify, type `pipenv --version` in command prompt
    1. To install pipenv, run `pip install --user pipenv`
    2. Once it's done, it will likely give you a message saying pipenv is located in `<some folder>\Python312\Scripts` which isn't on your path. You need to add pipenv to PATH
    3. Open `Edit the system environment variables` from the start menu. Searching for 'path' will likely bring it up
    4. Click `Environment Variables...`
    5. Select the 'Path' user variable and click Edit
    6. Click New, add the location mentioned in the pipenv installation
3. Make sure program files are in their own folder. Eg. `User\Documents\PDF Filler`
4. Open command prompt, navigate to the project folder
5. Run `pipenv install` from the project folder

Starting the program
===

1. Put desired PDFs in a folder called `forms` in the project folder
2. 
3. Fill in field that appear
4. Click save

-----

### Todo
* Finish README
* When the parent window changes size, resize components
* Add horizontal scrollbar to right side if needed
* Make hide field button more user friendly
* Add rename field button