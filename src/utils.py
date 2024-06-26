import yaml
import os
from os.path import join
import PyPDF2
from pathlib import Path
from src.logger import logging



def read_yaml(file_path):
    org_path= Path(file_path)
    try:
        with open(org_path, 'r') as file:
            #reading the yaml file and dumping into ouput
            #out_put ={}
            data = yaml.safe_load(file)
            #out_put  = yaml.dump(data, default_flow_style=False) 

        logging.info(f"{file_path} read sucessfully")
        return data

    except FileNotFoundError:
        logging.error(f"Error: File '{org_path}' not found.")
    except yaml.YAMLError as exc:
        logging.error(f"Error parsing YAML data: {exc}")



def read_pdf(file_path):
    org_path = Path(file_path)
    try:
        with open(org_path,"rb") as f:
            data = PyPDF2.PdfReader(f)
            num_pages = len(data.pages)

            # Loop through each page and extract text
            out_put=""
            for num in range(num_pages):
                page = data.pages[num]
                text = page.extract_text()
                out_put+=text
            #f.close()
        logging.info(f"{file_path} read sucessfully")   
        return out_put
    except FileNotFoundError:
        logging.error(f"Error: File '{org_path}' not found.")
    except Exception as e:
        logging.error(f"{e} error occured during reading a PDF file {file_path}")

