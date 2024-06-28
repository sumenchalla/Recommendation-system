from src.utils import read_yaml
from dataclasses import dataclass



data = read_yaml("D:\\Data Science\\Gen AI\\Recomender_system\\config.yaml") #You have change it in your local machine

@dataclass
class dataingestionconfig:
    ingestion_path = data["data_ingestion"]["path"]
    resume_url     = data["data_ingestion"]["resume_url"]
    projects_url   = data["data_ingestion"]["projects_url"]
    resume_path    = data["data_ingestion"]["resume_path"]
    project_path   = data["data_ingestion"]["project_path"]
    unzip_path     = data["data_ingestion"]["unzip_path"]

@dataclass
class datatransformationconfig:
    resumes        = data["data_transformation"]["resumes_path"]
    Trans_path     = data["data_transformation"]["df_path"]