Installation
===

1. Make sure python 3.12 is installed. To verify, type `python --version` in command prompt
    1. To install python, go to [python.org](https://www.python.org) and download python 3.12 or newer
    2. When installing, make sure to check the option for 'Add python to PATH'
2. Make sure pipenv is installed. To verify, type `pipenv --version` in command prompt
    1. To install pipenv, run `pip install --user pipenv`
    2. Once it's done, it will likely give you a message saying pipenv is located in `<user appdata>\Python312\Scripts` which isn't on your path. You need to add pipenv to PATH
    3. Open `Edit the system environment variables` from the start menu. Searching for 'path' will likely bring it up
    4. Click `Environment Variables...`
    5. Select the 'Path' user variable and click Edit
    6. Click New, add the location mentioned in the pipenv installation
3. Make sure program files are in their own folder. Eg. `User\Documents\PDF Filler`
4. Open command prompt, navigate to the project folder
5. Run `pipenv install` from the project folder

Program Setup
===

* Put PDFs in a folder called `forms` in the project folder  
    PDF folder structure will be duplicated in the program
* `ignore.cfg` contains field ids that the program will ignore. These won't be shown when loading PDFs
* `rename.json` contains mappings from internal field names to human-readable names. Any fields that have the same name will be combined in the program.  
    A field that doesn't appear in rename.json will use the internal field id for name matching and display

Usage
===

## Filling PDFs
Select PDFs from the list on the left, then press 'Load PDFs'. A list of fields will appear on the right side. Enter values in the entry boxes and press 'Save'. Filled PDFs will be saved to the `output` folder. If a value is entered in 'Output Subfolder', a folder with that name will be created in `output` and filled PDFs will be put there instead.  
The output folder layout will mimic the folder layout from the `forms` folder.

## Hiding Fields
The goal of the program is to fill in fields that are common across PDFs so values only need to be entered once. Some fields that only appear in one PDF may be better hidden from this program. For those fields click the 'Hide' button beside the undesired field. After confirmation an entry will be added to `ignore.cfg` and that field will be hidden in the future. To unhide a field, open `ignore.cfg` in notepad (or any text editor) and remove the row.

## Renaming Fields

The internal field names of a PDF aren't normally expected to be visible to a user. Sometimes those names are non descriptive or just messy to look at, and worse for this program they likely aren't the same name across different PDFs.  
When a field has a displayed/internal name that doesn't match what it should be, click the 'Rename' button for that field. A dialog box will open prompting you for a new name. Changing the name to match an existing field will make it so in the future, those fields will all take the same value as entered in the program.  
Renames are stored in `rename.json`. JSON keys are the internal field id, values are the display name to use for that field.

### The 'Map Fields' Button
In some cases, the internal field names are total nonsense, eg a field name like `001-1` doesn't tell you anything about what that field is supposed to be. If a field like that is found, you can select the PDF and click 'Map Fields'. The program will output PDFs to 'output/FieldMapping' with the field id filled in on the whole form. You can open the resulting PDF like normal, then see which field id corresponds to which expected value, then rename accordingly.

Issues/Todo
===
* Hiding or renaming fields when more than one field shares the display name will only update the first field with that display name. Visually the fields list will update as though only one field had that name, regardless of how many actually do.
* Renaming a field to an existing name won't combine rows
* Renaming fields should use a dropdown instead of text entry. That way display names can be guaranteed to match each other. Either a seperate entry for 'new name' can be added, or new names will need to be added to `rename.json` manually the first time.

-----

[github link](https://github.com/Malikil/pdf-filler)