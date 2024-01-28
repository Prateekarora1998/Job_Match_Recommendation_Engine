# Job Match Recommendation Engine

### Prerequisite

* Install Python. After the installation, type `python --version` in command prompt or terminal to check for the python installation.
* Run command prompt or terminal as an Administrator.
* Type `pip --version` to check for pip installation.
* Install 3 libariers using command prompt which are: Pandas, Pytest and Pyarrow.

    Windows:
    * `pip install pandas`
    * `pip install pytest`
    * `pip install pyarrow`
    
    Ubuntu/Mac OS:
    * `sudo pip install pandas`
    * `sudo pip install pytest`
    * `sudo pip install pyarrow`
* Type `pip list` or `pip3 list` to print the list of python libraries installed. If the above 3 libraries are installed, it will be displayed in the list.
* Install `git`.

Note: Pyarrow is not being used in the code. It is installed to resolve the warning which is as follows:

Warning: Pyarrow will become a required dependency of pandas in the next major release of pandas > (pandas 3.0), (to allow more performant data types, such as the Arrow string type, and > better interoperability with other libraries) but was not found to be installed on your > system.

As mentioned that Pyarrow will become a required dependency of pandas in the next major release of pandas, it is necessary to install this library inorder to avoid errors in future when pandas library is upgraded.

### Formatting of python files

I have applied Black Formatter to both python files.

### Steps to run the python files

* Open Command Prompt and locate to the drive/directory in which you want to clone the git repository
* Type `git clone https://github.com/Prateekarora1998/Job_Match_Recommendation_Engine.git` to clone the repository.
* Locate to the `Job_Match_Recommendation_Engine` folder using Command Prompt.
* Type `python -m pytest` in command prompt **to run the automated tests**.
* After successfully running the tests, type `python recommendationEngine.py` **to execute the python program**. This will display the results in command prompt.

