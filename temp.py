import os
import sys
from pathlib import Path
#from src.logger import logging

#setting the pathpoint to current folder
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/config/configuration.py",
    f"src/config/__init__.py",
    f"src/pipeline/__init__.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",


]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            print(f"Creating empty file: {filepath}")

    else:
        print(f"Error occured while creating {filedir} folder for {filename}")

