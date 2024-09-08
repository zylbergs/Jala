import pandas as pd
import streamlit as st
from vali_tools.valitools import check_health
from transform.feature_store import feature_store
from ml_prediction.biomass import predict_biomass
from report_sr import gen_report_sr
import pickle
import sys
import os

# Path to the transform folder
transform_path = os.path.abspath(os.path.join(os.getcwd(), 'transform'))

# Add the transform folder to the Python path
if transform_path not in sys.path:
    sys.path.append(transform_path)

# Import the feature_store module
from feature_store import feature_store

# Streamlit application
st.title("JALA Application")

# Button to call the feature_store function
st.write("Generate New Feature for feature store")
if st.button("Generate Features"):
    with st.spinner("Generating features..."):
        features = feature_store(gen_version=True)
        st.success("Features generated successfully!")
        st.write(features)

# Button to call the gen_report_sr function
st.write("Genereate Report SR & Average growth rate")
if st.button("Generate Report"):
    with st.spinner("Generating report..."):
        report = gen_report_sr()
        st.success("Report generated successfully!")
        with open("Report\SR_ADG_CYCLE.xlsx", "rb") as file:
            btn = st.download_button(
                label="Download Report",
                data=file,
                file_name="report.xlsx",
                mime="application/vnd.ms-excel"
            )
        st.write(report)

# Button to download the report
        st.download_button("Download Report", data="Report\SR_ADG_CYCLE.xlsx", file_name="SR_ADG_CYCLE.xlsx")

#
st.write("Download Template Data for prediction")
with open("devs\X_test.xlsx", "rb") as file:
  btn = st.download_button(
    label="Download Template",
    data=file,
    file_name="template.xlsx",
    mime="application/vnd.ms-excel"
  )

st.write("[ML MODEL] predict biomass")
# Create a file uploader
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the uploaded file
    test_data = pd.read_excel(uploaded_file)

    # Predict biomass
    with open(r"model_repo\biomass\model_biomass_version_20240907233653.pkl", 'rb') as file:
        model = pickle.load(file)
    prediction = predict_biomass(test_data, model)
    
    test_data['prediction'] = prediction
    test_data.to_excel("prediction.xlsx", index=False)

    with open("prediction.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download Result",
            data=file,
            file_name="prediction.xlsx",
            mime="application/vnd.ms-excel"
        )
        st.write(prediction)

st.write("[ML MODEL] predict SR")
# Create a file uploader
uploaded_file2 = st.file_uploader("Upload Excel file2", type=["xlsx"])

if uploaded_file2 is not None:
    # Read the uploaded file
    test_data = pd.read_excel(uploaded_file2)

    # Predict biomass
    with open(r"model_repo\sr\model_sr_version_20240907232416.pkl", 'rb') as file:
        model = pickle.load(file)
    prediction = predict_biomass(test_data, model)

    test_data['prediction'] = prediction
    test_data.to_excel("prediction.xlsx", index=False)

    with open("prediction.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download Result",
            data=file,
            file_name="prediction.xlsx",
            mime="application/vnd.ms-excel"
        )
        st.write(prediction)

st.write("[ML MODEL] predict sell price")
# Create a file uploader
uploaded_file3 = st.file_uploader("Upload Excel file3", type=["xlsx"])

if uploaded_file3 is not None:
    # Read the uploaded file
    test_data = pd.read_excel(uploaded_file3)

    # Predict biomass
    with open(r"model_repo\sellprice\model_sellprice_version_20240907233306.pkl", 'rb') as file:
        model = pickle.load(file)
    prediction = predict_biomass(test_data, model)

    test_data['prediction'] = prediction
    test_data.to_excel("prediction.xlsx", index=False)

    with open("prediction.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download Result",
            data=file,
            file_name="prediction.xlsx",
            mime="application/vnd.ms-excel"
        )
        st.write(prediction)

st.write("[ML MODEL] predict average harvest weight")
# Create a file uploader
uploaded_file4 = st.file_uploader("Upload Excel file4", type=["xlsx"])

if uploaded_file4 is not None:
    # Read the uploaded file
    test_data = pd.read_excel(uploaded_file4)

    # Predict biomass
    with open(r"model_repo\avg_harvest\model_avghar_version_20240907232920.pkl", 'rb') as file:
        model = pickle.load(file)
    prediction = predict_biomass(test_data, model)
    test_data['prediction'] = prediction
    test_data.to_excel("prediction.xlsx", index=False)

    with open("prediction.xlsx", "rb") as file:
        btn = st.download_button(
            label="Download Result",
            data=file,
            file_name="prediction.xlsx",
            mime="application/vnd.ms-excel"
        )
        st.write(prediction)
# Add text at the bottom of the page
st.write("Made with ❤️ by kevin")

