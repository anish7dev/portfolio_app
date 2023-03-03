import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Anish")
    content="""
    Hi, I am Anish! I am a python learner trying to develop a web app 
    and enhance my skills. Completed my B.tech in 2022 and currently working 
    as an Assistant Engineer in a Delhi-based company.Eager to learn new things 
    and incerase the productivity"
    """
    st.info(content)

content2="Below you can find some of the apps which i have build in the python.Feel free to contact me!"
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])


df=pd.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])  
        st.image("images/" + row["image"])  
        st.write(f"[Source code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])  
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")