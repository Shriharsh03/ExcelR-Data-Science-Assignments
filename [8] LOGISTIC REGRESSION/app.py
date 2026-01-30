import streamlit as st
import pandas as pd
import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diabetes Prediction App")
st.write("Logistic Regression Model")

pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 300, 120)
bp = st.number_input("Blood Pressure", 0, 200, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 33)

input_df = pd.DataFrame({
    "Pregnancies": [pregnancies],
    "Glucose": [glucose],
    "BloodPressure": [bp],
    "SkinThickness": [skin],
    "Insulin": [insulin],
    "BMI": [bmi],
    "DiabetesPedigreeFunction": [dpf],
    "Age": [age]
})

if st.button("Predict"):
    result = model.predict(input_df)
    if result[0] == 1:
        st.error("Prediction: Diabetic")
    else:
        st.success("Prediction: Not Diabetic")
