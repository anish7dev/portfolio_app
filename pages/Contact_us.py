import streamlit as st
from send_email import send_mail,smtplib,ssl
# import pandas

st.header("Contact Me")

with st.form(key="email"):
    user_email=st.text_input("Your Email adress")
    raw_msg=st.text_area("Your message")
    msg=f"""\
Subject:New email from {user_email}

From: {user_email}
{raw_msg}    
"""
    button= st.form_submit_button("Submit")
    if button:
        send_mail(msg)
        st.info("Your email was sent successfully")

# df=pandas.read_csv("bonus/topics.csv")

# with st.form(key="email"):
#     user_email=st.text_input("Your Email adress")
#     topic=st.selectbox("What topic do you want to discuss?",
#                        df["topic"])
#     raw_msg=st.text_area("Your message")
#     msg=f"""\
# Subject:New email from {user_email}

# From: {user_email}
# Topic:{topic}
# {raw_msg}    
# """
#     button= st.form_submit_button("Submit")
#     if button:
#         send_mail(msg)
#         st.info("Your email was sent successfully")