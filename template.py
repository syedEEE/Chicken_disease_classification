import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s:')
project_name = "CNNClassifier"

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "dvc.yaml",
    "params/yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file : {filename}")
    if not os.path.exists(filepath) or os.path.getsize(filedir) == 0:
        with open(file,'w') as f:
            logging.info("Creating the empty file")
    else:
        logging.info(f"{filename} is already exists")