import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: - %(levelname)s - %(message)s:")

project_name="disease_classification"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "main.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    file_dir, filename = os.path.split(filepath)


    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating directory {file_dir}: for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file {filepath}")
    
    else:
        logging.info(f"{filename} already exists.")