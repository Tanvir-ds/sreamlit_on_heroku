# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 18:19:48 2023

@author: Tanvir Ahmed
"""

#importing libraries
import pickle as pk
import streamlit as st
from streamlit_option_menu import option_menu

#laoding the saved model
diabates_model = pk.load(open('diabates_model.txt','rb'))

heart_model = pk.load(open('heart_model.txt','rb'))



#Creating sidebars for nevigation
with st.sidebar:
    nevigations = option_menu("Multiple Diseases Prediction System",
                              ["Diabates Prediction","Heart Diseases Prediction"],
                              icons=["activity","heart"],
                              default_index=0)


#Diabates Prediction Pages
if (nevigations=="Diabates Prediction"):
        
    #Setting the title
    st.title("Diabates Prediction using ML")
        
    #Getting input from users
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    #columns for input field
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies:")
    
    with col2:
        Glucose = st.text_input("Glucose Level:")
        
    with col3:   
        BloodPressure = st.text_input("Blood Pressure Value:")
        
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value:")
        
    with col2:
        Insulin = st.text_input("Insulin Value:")
        
    with col3:
        BMI = st.text_input("BMI Level:")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes PedigreeFunction Level:")
        
    with col2:
        Age = st.text_input("Age of the patient:")
    
    
    #result of the prediction
    result1 = ""
    
    #create a button for prediction
    if st.button("Diabates Test Result"):
        result1 = diabates_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        
        if (result1[0]==0):
            result1 = "The Person has no Diabatic."
        else:
            result1 = "The Person has Diabatic."
        
        
    st.success(result1)

        
        
#Heart Diseases Prediction  Pages
if (nevigations=="Heart Diseases Prediction"):
        
    #Setting the title
    st.title("Heart Diseases Prediction using ML")
     
    #Getting input from users
    #age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall
    #columns for input field
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age of the patient:")
    
    with col2:
        sex = st.text_input("Sex of the patient:")
        
    with col3:   
        cp = st.text_input("Cistolic Pressure Value:")
        
    with col1:
        trtbps = st.text_input("trtbps Value:")
        
    with col2:
        chol = st.text_input("chol Value:")
        
    with col3:
        fbs = st.text_input("fbs Value:")
        
    with col1:
        restecg = st.text_input("restecg Value:")
        
    with col2:
        thalachh = st.text_input("thalachh Value:")
        
    with col3:
        exng = st.text_input("exng Level:")
        
    with col1:
        oldpeak = st.text_input("oldpeak Value:")
        
    with col2:
        slp = st.text_input("slp Value:")
        
    with col3:
        caa = st.text_input("caa Level:")
        
    with col1:
        thall = st.text_input("thall Value:")
        
        
    #result of the prediction
    result2 = ""
    
    #create a button for prediction
    if st.button("Heart Diseases Test Result"):
        result2 = heart_model.predict(([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]]))
        
        
        if (result2[0]==0):
            result2 = "The Person has no Heart's Problem."
        else:
            result2 = "The Person has Heart's Problem."
        
        
    st.success(result2)