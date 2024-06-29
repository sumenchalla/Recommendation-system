import streamlit as st
import pickle
import os
from src.config.configuration import datatransformationconfig,dataingestionconfig
from src.pipeline.recommendation_pipeline import Reco_pipeline
import glob
from src.utils import read_pdf

trans= datatransformationconfig()
inge_config = dataingestionconfig()
Recommend = Reco_pipeline()

st.header("Talent recommendation system")
embedings1 = pickle.load(open(os.path.join(trans.Trans_path,"embedings\\embedings1.pkl"),"rb"))
embedings2 = pickle.load(open(os.path.join(trans.Trans_path,"embedings\\embedings2.pkl"),"rb"))
embedings3 = pickle.load(open(os.path.join(trans.Trans_path,"embedings\\embedings3.pkl"),"rb"))


model1 = pickle.load(open(os.path.join(trans.Trans_path,"models\\model1.pkl"),"rb"))
model2 = pickle.load(open(os.path.join(trans.Trans_path,"models\\model2.pkl"),"rb"))
model3 = pickle.load(open(os.path.join(trans.Trans_path,"models\\model3.pkl"),"rb"))

project_files = glob.glob(os.path.join(os.path.join(inge_config.ingestion_path,"Projects"), '*.pdf'))
projects = []

for i in range(len(project_files)):
    projects.append(project_files[i].split("\\")[7].removesuffix(".pdf"))

project=st.selectbox(
    "Select one projecct from drop down",
    projects
)
idx = project_files.index(os.path.join(inge_config.ingestion_path,"Projects\\")+project+".pdf")

if project:
    data=read_pdf(project_files[idx])
    text = st.text_area(label="This is the description of selected project if required you can modify it",value=data,height=400)



model_list =["multi-qa-MiniLM-L6-cos-v1","all-MiniLM-L12-v2","all-MiniLM-L6-v2"]

model_select = st.selectbox(
        "slecect your model",
        model_list
)

model = None
embedings = None
if model_select == "multi-qa-MiniLM-L6-cos-v1":
    model = model1
    embedings= embedings1
elif model_select == "all-MiniLM-L12-v2":
    model = model2
    embedings = embedings2
else:
    model = model3
    embedings= embedings3

if st.button("Recommend"):
    names=Recommend.recommend(data=text,model=model,embedings=embedings)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image("OIP.jpeg")
    with col2:
        st.text(names[1])
        st.image("OIP.jpeg")
    with col3:
        st.text(names[2])
        st.image("OIP.jpeg")
    with col4:
        st.text(names[3])
        st.image("OIP.jpeg")
    with col5:
        st.text(names[4])
        st.image("OIP.jpeg")


