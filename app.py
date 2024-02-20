import pandas as pd
import streamlit as st
import numpy as np
import pickle
import datetime

with open('car_price_predictor_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.title(":blue[Car Price Predictor] :car:")
st.subheader("**Are You Planning To Sell Your Car?**\n")
st.markdown("#### So Let's try Evaluating The Price ####\n")
s1=st.number_input("What is The Current Ex-Showroom price For Car (In Lakhs)? ",0.0,25.0,step=0.5)
s2=st.number_input("What is Distance Traveled (In Kms)? ",100,500000,step=100)
s3=st.selectbox("What is Fuel Type Of Car? ",("Petrol","Diesel","CNG"))

if s3=="Petrol":
    s3=0
elif s3=="Diesel":
    s3=1
elif s3=="CNG":
    s3=2


s4=st.selectbox("Are You A Dealer Or Individual? ",("Individual","Dealer"))
if s4=="Individual":
    s4=1
elif s4=="Dealer":
    s4=0

s5=st.selectbox("What is Transmission Type? ",("Manual","Automatic"))
if s5=="Manual":
    s5=0
elif s5=="Automatic":
    s5=1


s6=st.slider("No. of Owners Car Previously have? ",0,5)

date_time=datetime.datetime.now()

years=st.number_input("In Which Year Car Was Purchased ",1950,date_time.year)
s7=date_time.year-years

if st.button("Predict Price"):
      query_data = {
        'Present_Price': [s1],
        'Kms_Driven': [s2],
        'Fuel_Type': [s3],
        'Seller_Type': [s4],
        'Transmission': [s5],
        'Owner': [s6],
        'Age': [s7],
        }
      
      query_df = pd.DataFrame(query_data)

      prediction = float(round(np.exp(loaded_model.predict(query_df)[0]),2))

      st.subheader(f"The Predicted Price For Your Car Is: :green[{prediction}]")
   






