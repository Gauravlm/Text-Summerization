import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="textSummerizer"

list_of_files=[
    '.github/workflow/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/conponents/__init__.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirement.txt',
    'setup.py',
    'notebooks/test.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename= os.path.split(filepath)
    

    # create new folder/dir
    # if not os.path.exists(filedir):
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the filename{filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        # (os.path.getsize(filepath)==0) --> if file already content code then it will not create file
        
        # to create empty file
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating file: {filepath}')
    else:
        logging.info(f'File is already exists: {filepath}')









