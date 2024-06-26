import os
from src.config.configuration import dataingestionconfig
from src.logger import logging
import urllib
import zipfile



#ingestion = dataingestionconfig()
class Data_Ingestion:
    def __init__(self):
        self.ingestion = dataingestionconfig()

    def download_files(self):
        try:
            resume_url = self.ingestion.resume_url
            zip_download_dir = self.ingestion.resume_path
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)
            logging.info(f"Downloading data from {resume_url} into file {zip_download_dir}")

            urllib.request.urlretrieve(resume_url, zip_download_dir)

        except Exception as e:
            logging.error(f"Error occured during downloading from {resume_url}")
            raise e
        
        try:
            resume_url = self.ingestion.projects_url
            zip_download_dir = self.ingestion.project_path
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)
            logging.info(f"Downloading data from {resume_url} into file {zip_download_dir}")

            urllib.request.urlretrieve(resume_url, zip_download_dir)

        except Exception as e:
            logging.error(f"Error occured during downloading from {resume_url}")
            raise e
        
    def unzip_file(self):
        try:
            unzip_path = os.path.join(self.ingestion.unzip_path,"Resumes")
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.ingestion.resume_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logging.info(f"Extracting file from {self.ingestion.project_path} done")

        except Exception as e:
            logging.error(f"Error occured while extracting file from {self.ingestion.resume_path}")
            raise e   
        try:
            unzip_path = os.path.join(self.ingestion.unzip_path,"Projects")
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.ingestion.project_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logging.info(f"Extracting file from {self.ingestion.project_path} done")

        except Exception as e:
            logging.error(f"Error occured while extracting file from {self.ingestion.project_path}")
            raise e      