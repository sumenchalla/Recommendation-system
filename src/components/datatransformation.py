from src.config.configuration import dataingestionconfig
from src.config.configuration import datatransformationconfig
from src.utils import read_pdf
import os
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import glob
import json
import pandas as pd
from src.logger import logging
from sentence_transformers import SentenceTransformer
import pickle




# Loading environment variables from .env file for keeping api key to be private
load_dotenv()
# Get the Hugging Face API key
api_key = os.getenv("HUGGINGFACE_API_KEY")

prompt_template="""
Your a resume summarization expert. Given the content {content} of resume your job is to identify the \
name , skills, cerifications and past projects details of the candidate and give the identified things to user\
Make sure to format your response like : 

Answer start:
{{
    "name"    : "name of the candidate here",
    "skills"  : "skills of the candidate that are mentioned in the resume ",
    "projects": ["description  of project 1 of candidate that is mentioned in resume","description  of project 2 of candidate that is mentioned in resume",.......],
    "certifications" : "certifications of the candidate that are mention in the resume"
    "internships"    : "Industry related internships or job experince of candidate that are mentioned in the resume"
}}

answer ends.
Please give answer in required formate only dont add any text or any code for your answer and stop generating further text and end your answer with flower bracket.

"""

class Data_Transformation:
    def __init__(self):
        self.ingestion = dataingestionconfig()
        self.transformation = datatransformationconfig()

    def resumes_to_dataframe(self):
        try:
            prompt=PromptTemplate(input_variables=["content"],template=prompt_template)
            repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"

            llm_client = InferenceClient(model=repo_id, timeout=120,token=api_key)
            logging.info(f"{repo_id} model is sucessfully loaded")

        except Exception as e:
            logging.error(f"{e} error occured while loading {repo_id} model")

        try:
            folder_path = self.transformation.resumes

            pdf_files = []

            # Use glob to find all PDF files in the specified folder
            pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))
            dict_list=[]
            for i in pdf_files:
                data = read_pdf(i)
                prom = prompt.format(content=data)
                answer = llm_client.text_generation(prom,max_new_tokens=1000,)
                if answer.startswith("Answer start:\n"):
                    answer = answer.removeprefix("Answer start:\n")
                #print(answer)
                data_dict = json.loads(answer.replace("\n","").split("}")[0]+"}")
                dict_list.append(data_dict)
            logging.info("list of dictotnaries which contains resume details are sucessfully created")

        except Exception as e:
            logging.error(f"{e} error occured while creating dict_list")

        try:
            df = pd.DataFrame(dict_list)
            for i in range(len(df["projects"])):
                project =""
                for j in df["projects"][i]:
                    project+=j
                df["projects"][i]=project

        except Exception as e:
            logging.error(f"{e} error occured during conversion of dict_list into dataframe")

        os.makedirs(self.transformation.Trans_path,exist_ok=True)

        df.to_csv(os.path.join(self.transformation.Trans_path,"data.csv"),index=False)

        logging.info("Resumes data sucessfully converted to DataFrame")

    def resume_cleaning(self):

        try:
            df = pd.read_csv(os.path.join(self.transformation.Trans_path,"data.csv"))
            df.fillna("",inplace=True)
            df["description"] = ""
            for i in range(len(df["name"])):
                df["description"][i]=df["skills"][i]+ " "+ df["projects"][i]+ " "+ df["certifications"][i]+" " + df["internships"][i]
            df["description"] = df["description"].apply(lambda row: str(row).replace("[","").replace("]","").replace("|","").replace("'","").replace(",",""))
            logging.info("Data frame was sucessfully cleaned")
        except Exception as e:
            logging.error(f"{e} error occured while cleaning the DataFrame")
        

        try:

            model1 = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")
            model2 = SentenceTransformer("all-MiniLM-L12-v2")
            model3 = SentenceTransformer("all-MiniLM-L6-v2")
            embedings1 = model1.encode(df["description"])
            embedings2 = model2.encode(df["description"])
            embedings3 = model3.encode(df["description"])

            logging.info("Embedings for the description was created sucessfully")

        except Exception as e:
            logging.error(f"{e} error occured during creation of embedings of description")

        try:
            os.makedirs(os.path.join(self.transformation.Trans_path,"models"),exist_ok=True)
            os.makedirs(os.path.join(self.transformation.Trans_path,"embedings"),exist_ok=True)

            with open(os.path.join(self.transformation.Trans_path,"models\\model1.pkl"),"wb") as f:
                pickle.dump("model1.pkl",f)
            with open(os.path.join(self.transformation.Trans_path,"models\\model2.pkl"),"wb") as f:
                pickle.dump("model2.pkl",f)
            with open(os.path.join(self.transformation.Trans_path,"models\\model3.pkl"),"wb") as f:
                pickle.dump("model3.pkl",f)
            with open(os.path.join(self.transformation.Trans_path,"embedings\\embedings1.pkl"),"wb") as f:
                pickle.dump("embedings1.pkl",f)
            with open(os.path.join(self.transformation.Trans_path,"embedings\\embedings2.pkl"),"wb") as f:
                pickle.dump("embedings2.pkl",f)
            with open(os.path.join(self.transformation.Trans_path,"embedings\\embedings3.pkl"),"wb") as f:
                pickle.dump("embedings3.pkl",f)   


        except Exception as e:
            logging.error(f"{e} error occured during saving models and embedings")