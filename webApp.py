# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:26:12 2023

@author: user
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("trained_model.sav","rb"))


#Creating a function for prediction

def calories_prediction(input_data):

    #change input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=object)

    my_reshaped = input_data_as_numpy_array.reshape(1,7)

    prediction = loaded_model.predict(my_reshaped)
    
    return f"You burnt {prediction[0]} calories today"



def main():
    #giving a title
    st.title("Burnt Calories App")
    
    #Getting input data from user
    # Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp
    Gender = st.text_input("What is your gender?")
    if (Gender=="male"):
        Gender = 0
    else:
        Gender = 1
    Age = st.text_input("How old are you?")
    Height = st.text_input("What is your height?")
    Weight = st.text_input("What is your weight?")
    Duration = st.text_input("For how long do you exercise?")
    Heart_Rate = st.text_input("What is your heart rate?")
    Body_Temp = st.text_input("What is your body temperature?")
    
    #Prediction
    loss = ''
    
    if st.button("Calories Burnt Result"):
        loss = calories_prediction([Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp])

    st.success(loss)


if __name__=="__main__":
    main()
















