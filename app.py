# import sklearn
import numpy as np
import pickle as pkl
import streamlit as st
import pandas as pd

test = ['Maruti Suzuki Swift', 'Maruti',2019,100, 'Petrol']


if __name__ == '__main__':
    loaded_model = pkl.load(open('LinearRegressionModel.pkl', 'rb'))
    st.title("Predicting Car Price")
    input_name = st.text_input("Enter the car details :")
    input_company = st.text_input("Enter the car company :")
    input_year = st.text_input("Enter the car year :")
    input_kms = st.text_input("Enter the car kms :")
    input_fuel = st.text_input("Enter the car fuel :")

    if st.button("Predict"):
        data = pd.DataFrame([[input_name, input_company, input_year, input_kms, input_fuel]], columns=['name','company','year','kms_driven','fuel_type'])
        try:
            prediction = loaded_model.predict(data)
            st.success('Price of the car {}'.format(prediction))
        except:
            st.error('Please enter valid data')
