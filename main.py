
import os 
from posixpath import basename
from shutil import move
from dotenv import load_dotenv
load_dotenv()

root_dir = os.getenv('ROOT_DIR')
job_apps_dir = os.getenv('JOBAPPS_DIR')
misc_dir = os.getenv('MISC_DIR')

filter_words = os.getenv('FILTER_WORDS').split(',')


files = []
for f in os.listdir(root_dir):
    if f.endswith('.pdf'):
        files.append(f)

# moves files in root_dir to job_apps_dir if they contain filter_words
for file in files:
    path = root_dir + "/" + file
    basename = os.path.basename(path)
    #print(basename)
    basename_splited = basename.lower().split("_")
    #print(basename_splited)
    for word in basename_splited:
        if word in filter_words:
            move(path, job_apps_dir + "/" + basename)
            print (f"Moved {basename} to {job_apps_dir}")
            break



