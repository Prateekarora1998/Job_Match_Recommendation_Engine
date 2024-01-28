# Job Match Recommendation Engine

Steps to execute the python code and test are given as follows:

### Prerequisite

* Install Python. You can download the .exe file to install the python from the offical python site. After the installation, type `python --version` in command prompt or terminal to check if python has been installed or not.
* Type `pip --version` to check for pip installation.
* Install 3 libariers which are: Pyarrow, Pandas and Pytest.

    Windows:
            pip install pandas
            pip install pyarrow
            pip install pytest
    
    Ubuntu/Mac OS:
            sudo pip install pandas
            sudo pip install pyarrow
            sudo pip install pytest
* Type `pandas --version`, `pyarrow --version`, `pytest --version` to check for the installation.
* Install `git`.

Note: Pyarrow is not being used in the code. It is should be installed to resolve the Warning error which is as follows:

Warning: Pyarrow will become a required dependency of pandas in the next major release of pandas > (pandas 3.0), (to allow more performant data types, such as the Arrow string type, and > better interoperability with other libraries) but was not found to be installed on your > system.

Moreover, as mentioned that Pyarrow will become a required dependency of pandas in the next major release of pandas, it is necessary to install this library inorder to avoid errors in future when pandas library is upgraded.

### Formatting of python files

I have applied Black Formatter to both python files.

### Steps to run the python files

* Open Command Prompt and locate to the drive/directory in which you want to clone the git repository
* Type `git clone https://github.com/Prateekarora1998/Job_Match_Recommendation_Engine.git` to clone the repository.
* Locate to the `Job_Match_Recommendation_Engine` folder using Command Prompt.
* Type `pytest` in command prompt to run the automated tests.
* After successfully running the tests, type `python recommendationEngine.py` to execute the python program. This will display the results in command prompt.

