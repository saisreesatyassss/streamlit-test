import streamlit as st
import pandas as pd


imgUrl="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1530&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

with st.sidebar:
    st.title("Auto ML")
    st.image(imgUrl, width=150)
    choice=st.radio("Navigation", ["Upload Data", "Profiling", "Ml", "Download Model"])
    st.info("This application is created by [  SAISRISATYA ](https://www.linkedin.com/in/padala-sai-sri-satya-subramaneswar-359998247/)")



if choice =="Upload Data":
    st.title("Upload Data for the Modeling")
    st.write("upload only CSV files.")
    file = st.file_uploader("Upload file", type=["csv"])
    if file:
        df=pd.read_csv(file,index_col=None)
        df.to_csv("UploadedData.csv",index=False)
        st.dataframe(df)
    


    
        