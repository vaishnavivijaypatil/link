import streamlit as st
import pandas as pd
import re
from datetime import date

st.set_page_config(page_title="Form Registration")
st.markdown("<h1><u><center>Regitrastion Form</h1></u></center>",unsafe_allow_html=True)
f_name,m_name,l_name=st.columns(3)
with f_name:
   f_name=st.text_input("",placeholder="Enter your First name",label_visibility="collapsed")
with m_name:
   m_name=st.text_input("",placeholder="Enter your Middle name",label_visibility="collapsed")
with l_name:
   l_name=st.text_input("",placeholder="Enter your Last name",label_visibility="collapsed")
email,number=st.columns(2)
with email:
   email=st.text_input("",placeholder="Enter your Correct email-ID",label_visibility="collapsed")
with number:
   number=st.text_input("",placeholder="Enter your phone number",label_visibility="collapsed")
col1,col2=st.columns(2)
with col1:
   min_date=date(2000,1,1)
   max_date=date.today()
   col1=st.date_input("Enter your date of birth :",min_value=min_date,max_value=max_date)
with col2:
   col12=st.selectbox("Select Course :",["CO-Computer engineering","IF-Information technology","CE-Civil engineering"])
uploaded_image=st.file_uploader("Upload an image",type=["jpg","png","jpeg"])
def validate_name(name,patten):
   if re.match(patten,name):
      return True
   else:
      return False
   
def validate_email(emai):
   pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
   if re.match(pattern,email):
      return True
   else:
      return False

def validate_phone_number(number):
   pattern=r"^(\+91|0)?[6789]\d{9}"
   if re.match(pattern,number):
      return True
   else:
      return False
   
f_name_pattern=r"^[a-zA-Z\s'-]+$"
m_name_pattern=r"^[a-zA-Z]+$"
l_name_pattern=r"[a-zA-Z]+$"


s_state=st.button
if st.button("Save"):
  
   if validate_name(f_name,f_name_pattern):
     st.write("")
   else:
         st.warning("please eneter a valid first name")

   if validate_name(m_name,m_name_pattern):
      st.write("")
   else:
      st.warning("Please enter valid middle name")

   if  validate_name(l_name,l_name_pattern):
      st.write("")
   else:
      st.warning("please enter a valid last name")

   if  validate_email(email):
      st.write("")
   else:
      st.warning("Please enter valid email-ID")
      
   if validate_phone_number(number):
      st.write("")
   else:
      st.warning("Please enter valid Phone number")
   
if s_state:
      if st.button("Submit"):
        if uploaded_image is not None:
           image_path=uploaded_image.name
           with open (image_path,"wb") as f:
              f.write(uploaded_image.getvalue())
           data={" First name":[f_name],"Middle name":[m_name],"Last name":[l_name],"Email-id":[email],"Phone no":[number],"Date of birth":[col1],"Course":[col2],"Image":[uploaded_image]}
           df=pd.DataFrame(data)
           df.to_csv("user_data.csv",index=False)
           st.success("Successfully completed!")
      
          