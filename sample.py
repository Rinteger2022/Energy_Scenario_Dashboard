import streamlit as st
import pandas as pd
import numpy as np
#df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
#df

#your_name = st.text_input("Number")
#if your_name:
#  df[df['phone'] == your_name]
    #st.write("There is some value. Processing...")

df=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1840897213&single=true&output=csv")
#print(df['Contact Number'])
#your_name=st.text_input("Number",value=8075311214)
#res = df.isin([your_name]).any().any()

#if res :
#   st.write("This value exists in Dataframe")

#else :
#   st.write("This value does not exists in Dataframe")

#if __name__ == '__main__':
 #   input = st.empty()
 #   txt = input.text_input("Insert number:")
  #  bt = st.button("Search")

 #   if bt:
  #      txt = "Search"
        #input.text_input("Insert text:", value=txt)
#        res = df.isin([txt]).any().any()
 #       if res :
 #         st.write("This value exists in Dataframe")
 #       else :
 #         st.write("This value does not exists in Dataframe")
    
    
    
#CompanyName=st.text_input("Company")
#Brandname=st.text_input("Brand")
#ContactNumber=st.text_input("Number")

if __name__ == '__main__':
    input = st.empty()
    input1 = st.empty()
    input2 = st.empty()
    txt = input.text_input("Insert Brand:")
    txt1 = input1.text_input("Insert Company:")
    txt2 = input2.text_input("Insert Number:")
    bt = st.button("Search")
    if bt:
        txt = "Search"
        input.text_input("Insert Brand:", value=txt)
        input.text_input("Insert Company:", value=txt1)
        input.text_input("Insert Number:", value=txt2)
        res = df.isin([txt,txt1,txt2]).any().any()

        if res :
          st.write("\nThis value exists in Dataframe")

        else :
         st.write("\nThis value does not exists in Dataframe")
