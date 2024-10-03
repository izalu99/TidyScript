# TidyScript

This script is designed to organize PDF files in a specified root directory by moving them to a job applications directory if their filenames contain certain filter words. The filter words, directories, and other configurations are specified in an .env file.


## Prerequisites
- Python 3.x
- python-dotenv package

You can install the python-dotenv package using pip:

```{pwsh}
pip install python-dotenv
```


## How to Use
You can download this script or clone it.

### Downloading
1. Download the script file from the repository.
2. Place the script in the directory where you created the .env file.

### Cloning
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
```
git clone https://github.com/izalu99/TidyScript.git
```
4. Navigate to the cloned directory:
```
cd TidyScript
```


### Configuration and Customization
1. Create a folder in your desired directory
2. Get the directory of the files you want organized into the new folder you just created.

3. Create a .env file in the same directory as your script with the following content:
```{}
ROOT_DIR=path/to/your/root/directory
JOBAPPS_DIR=path/to/your/job/applications/directory
MISC_DIR=path/to/your/miscellaneous/directory
FILTER_WORDS=resume,coverletter, cv, etc...
```
4. Replace the paths and filter words with your desired values.
5. You can change the variable names in the script to match your folder names if youd like.


### Running the Script
1. Ensure you have your .env file configured (See Configuration and Customization section).
2. Open your terminal or command prompt.
3. Navigate to the directory that has the script and the .env file.
4. Run the script using Python:
```
python main.py
```
5. The script will process the pdf files in the root directory and move them to directory you want if their filenames contain any of the filterwords.