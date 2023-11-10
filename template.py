import os 
from pathlib import Path
import logging

# Setting up the logging
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]:%(message)s:')
#Format could be FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s' where client IP, username can also be recorded recorded

project_name = "SOC-Estimation"

#We can automatize the process of creating required files and folders with the following code: 

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filename in list_of_files:
    filepath = Path(filename)  #Converting the file path to a Path object because different OS has different ways to organize paths. 
    filedir,filename = os.path.split(filepath) #separate the directory and filename components of the file path. 

#Lets first create the directory if it does not exist already 
    if filedir !="": 
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"Creating directory:{filedir} for the file {filename}")       
    
#Creating files if they dont exist or are empty
    if (not os.path.exists(filepath) or os.path.getsize(filepath)== 0): 
        with open(filepath, "w") as f:  #opens the file at filepath in write mode ("w"). If the file doesn't exist, it will be created.
            pass 
            logging.info(f"creating empty file:{filepath}")
    else:
            logging.info(f"{filename} is already exists") #In order to prevent duplicate files and folders.
        
