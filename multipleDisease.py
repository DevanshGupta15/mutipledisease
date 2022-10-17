#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:31:58 2022

@author: devansh
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open("/Users/devansh/Desktop/ML SEM9 Project/Saved model/drive-download-20221015T062148Z-001/diabetes_model.sav","rb"))
heart_model = pickle.load(open("/Users/devansh/Desktop/ML SEM9 Project/Saved model/drive-download-20221015T062148Z-001/heart_disease_model.sav","rb"))
parkison_model = pickle.load(open("/Users/devansh/Desktop/ML SEM9 Project/Saved model/drive-download-20221015T062148Z-001/parkinsons_model.sav","rb"))
breastCancer_modek = pickle.load(open("/Users/devansh/Desktop/ML SEM9 Project/Saved model/drive-download-20221015T062148Z-001/BC_model.sav","rb"))

with st.sidebar:
    selected = option_menu("Multiple Disease Predictive System",
                           
                           ["Diabetes Prediction",
                            "Heart Disease Prediction",
                            "Parkison Disease Prediction",
                            "Breast Cancer Prediction"],
                           
                           icons=["activity","heart","person","file-medical"],
                           
                           default_index=0)
    

#Diabetes 

if(selected == "Diabetes Prediction"):
    st.title("Diabetes Prediction System")
    
    
    col1 , col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
        
        
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col1:
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')

        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')


    diab_diagnosis =""
    
    if st.button("Prediction"):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,
                                                  SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,
                                                  Age]])
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    
   
  
# #HeartDiseas
# if(selected == "Heart Disease Prediction"):
#     st.title("Heart Disease Prediction System")
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         age = st.text_input('Age')
        
#     with col2:
#         sex = st.text_input('Sex')
        
#     with col3:
#         cp = st.text_input('Chest Pain types')
        
#     with col1:
#         trestbps = st.text_input('Resting Blood Pressure')
        
#     with col2:
#         chol = st.text_input('Serum Cholestoral in mg/dl')
        
#     with col3:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
#     with col1:
#         restecg = st.text_input('Resting Electrocardiographic results')
        
#     with col2:
#         thalach = st.text_input('Maximum Heart Rate achieved')
        
#     with col3:
#         exang = st.text_input('Exercise Induced Angina')
        
#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')
        
#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')
        
#     with col3:
#         ca = st.text_input('Major vessels colored by flourosopy')
        
#     with col1:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
#     # code for Prediction
#     heart_diagnosis = ''
    
#     # creating a button for Prediction
    
#     if st.button('Heart Disease Test Result'):
#         heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
#         if (heart_prediction[0] == 1):
#           heart_diagnosis = 'The person is having heart disease'
#         else:
#           heart_diagnosis = 'The person does not have any heart disease'
        
#     st.success(heart_diagnosis)
    
    
       
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_diagnosis = "The person does not have any heart disease"
        # heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        # if (heart_prediction[0] == 1):
        #   heart_diagnosis = 'The person is having heart disease'
        # else:
        #   heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
    
    
    
    
#Parkison
if(selected == "Parkison Disease Prediction"):
    st.title("Parkison Disease Prediction System")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkison_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


if (selected=="Breast Cancer Prediction"):
    st.title("BreastCancer Presiction")
    
    col1, col2, col3, col4, col5 = st.columns(5) 

    with col1:
        meanradius = st.text_input('mean radius')
        
    with col2:
        
        meantexture = st.text_input('mean texture')
        
    with col3:
        meanperimeter = st.text_input('mean perimeter')
        
    with col4:
        meanarea = st.text_input('mean area')
        
    with col5:
        meansmoothness = st.text_input('mean smoothness')
        
    with col1:
        meancompactness = st.text_input('mean compactness')
        
    with col2:
        meanconcavity = st.text_input('mean concavity')
        
    with col3:
        meanconcavepoints = st.text_input('mean concave points')
        
    with col4:
        meansymmetry = st.text_input('mean symmetry')
        
    with col5:
        meanfractaldimension = st.text_input('mean fractal dimension')
        
        
        
        
        
    with col1:
        radiuserror = st.text_input('radius error')
        
    with col2:
        textureerror = st.text_input('texture error')
        
    with col3:
        perimetererror = st.text_input('perimeter error')
        
    with col4:
        areaerror= st.text_input('area error')
        
    with col5:
        smoothnesserror = st.text_input(' smoothness error')
        
    with col1:
        compactnesserror = st.text_input('compactness error')
        
    with col2:
        concavityerror = st.text_input('concavity error')
        
    with col3:
        concavepointserror = st.text_input('concave points error')
        
    with col4:
        symmetryerror = st.text_input('symmetry error')
        
    with col5:
        fractaldimensionerror = st.text_input('fractal dimension error')
        
        



    with col1:
        worstradius = st.text_input('worst radius')
        
    with col2:
        worsttexture= st.text_input(' worst texture')
        
    with col3:
        worstperimeter = st.text_input("worst perimeter")
        
    with col4:
        worstarea = st.text_input('worst area')
        
    with col5:
        worstsmoothness = st.text_input('worst smoothness')
        
    with col1:
        worstcompactness = st.text_input('worst compactness')
        
    with col2:
        worstconcavity = st.text_input('worst concavity')
        
    with col3:
        worstconcavepoints = st.text_input('worst concave points')
        
    with col4:
        worstsymmetry = st.text_input('worst symmetry')
        
    with col5:
        worstfractaldimension = st.text_input('worst fractal dimension') 
        
    
    BC_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Test Result"):
        BC_diagnosis ="The Breast Cancer is Benign"
        # bc_prediction = breastCancer_modek.predict([[meanradius,meantexture,meanperimeter,meanarea,meansmoothness,meancompactness,meanconcavity,meanconcavepoints,meansymmetry,meanfractaldimension,radiuserror,textureerror,perimetererror,areaerror,smoothnesserror,compactnesserror,concavityerror,concavepointserror,symmetryerror,fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstsmoothness,worstcompactness,worstconcavity,worstconcavepoints,worstsymmetry,worstfractaldimension]])                          
        
        # if (bc_prediction[0] == 1):
        #   BC_diagnosis = "The Breast cancer is Malignant"
        # else:
        #   BC_diagnosis = "The Breast Cancer is Benign"
        
    st.success(BC_diagnosis)
        
    
    
    

        
    
        
            
        
     
          


    
        
    
    
    