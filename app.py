import streamlit as st
import pandas as pd
import joblib 
import numpy as np

st.header("Churn Dataset Prediction")

import pandas as pd
import streamlit as st

from sklearn.preprocessing import LabelEncoder, StandardScaler



# CustomerID,Age,Gender,Tenure,Usage Frequency,Support Calls,Payment Delay,Subscription Type,Contract Length,Total Spend,Last Interaction,Churn
# Get user inputs from Streamlit
actual_CustomerID =st.number_input("Enter Customer ID")
actual_Age =st.number_input("Enter Age")
actual_Gender =st.text_input("Enter Gender")
actual_Tenure =st.number_input("Enter Tenure")
actual_UsageFrequency =st.number_input("Enter Tenure Frequency")
actual_SupportCalls =st.number_input("Enter Support Calls")
actual_PaymentDelay = st.number_input("Enter Payment Delay")
actual_SubscriptionType=st.text_input("Enter Subscription Type")
actual_ContractLength=st.text_input("Enter Contract Length")
actual_TotalSpend = st.number_input("Enter Total Spend")
actual_LastInteraction=st.number_input("Enter Last Interaction")
un = st.number_input('enter a number')




# Create a DataFrame 

df = pd.DataFrame({
    'Unnamed: 0':[un],
    'CustomerID': [actual_CustomerID],
    'Age': [actual_Age],
    'Gender': [actual_Gender],
    'Tenure': [actual_Tenure],
    'Usage Frequency': [actual_UsageFrequency],
    'Support Calls': [actual_SupportCalls],
    'Payment Delay': [actual_PaymentDelay],
    'Subscription Type': [actual_SubscriptionType],
    'Contract Length': [actual_ContractLength],
    'Total Spend': [actual_TotalSpend],
    'Last Interaction': [actual_LastInteraction]
   
})

#  Display DataFrame in Streamlit
st.write(df)
label_encoders = {}
categorical_cols = ['Gender', 'Subscription Type', 'Contract Length']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


import joblib

model = joblib.load(r'C:\Users\Dell\OneDrive\Desktop\x\Models\best_model')

pred  = model.predict(df)

sumbit = st.button('press to see prediction')
if sumbit:
    st.subheader("The Prediction Is..")
    st.write(pred)

if pred==0:
    st.write("You Have No!!!")
else:
    st.write("You Have!!!")