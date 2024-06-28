from src.components.datatransformation import Data_Transformation
from sentence_transformers import util
import torch
import os
from src.config.configuration import datatransformationconfig
import pandas as pd

trans = datatransformationconfig()
tarnsform =  Data_Transformation()
tarnsform.resumes_to_dataframe()
tarnsform.resume_cleaning()

df= pd.read_csv(os.path.join(trans.Trans_path,"data.csv"))



class Reco_pipeline:
    def __init__(self):
        pass

    def recommend(self,data,model,embedings):

        embed = model.encode(str(data)) 
        scores = util.cos_sim(embed,embedings)
        top = torch.topk(scores,k=5,sorted=True)
        out=[]
        for i in top.indices[0]:
            out.append(df["name"][int(i)])
        return out

