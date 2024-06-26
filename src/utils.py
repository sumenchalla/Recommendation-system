import yaml
import os
from os.path import join
import pyPDF2
from pathlib import Path



def read_yaml(file_path):
    org_path= Path(file_path)

    with open(org_path,"r") as f:
        data = yaml.load_safe(f)
    return data
