from src.components.datatransformation import Data_Transformation
from sentence_transformers import util
import torch



class Reco_pipeline:
    def __init__(self):
        self.tarnsform =  Data_Transformation()

    def recommend(self,data,model,embedings):
        self.tarnsform.resumes_to_dataframe()
        self.tarnsform.resume_cleaning()

        embed = model.encode(data) 
        scores = util.cos_sim(embed,embedings)
        top = torch.topk(scores,k=5,sorted=True)

