import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
    
]
for filepath in list_of_files:
    filepath=Path(filepath) #this will take care if the default path in windows,mac,unix(/ or \)
    filedir, filename=os.path.split(filepath)# this will split the directory and file name

    #two variable, filedir is storing the dir and filename is storing the name of the file VIA split

    #creating folder
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating  directory; {filedir} for the file{filename}")

    #creating the file

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    

    else:
        logging.info(f"{filename}already exists")
