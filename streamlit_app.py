import pandas as pd
import streamlit as st
from vali_tools.valitools import check_health
from transform.feature_store import feature_store
from report_sr import gen_report_sr
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
if st.button("Generate Features"):
    with st.spinner("Generating features..."):
        features = feature_store(gen_version=True)
        st.success("Features generated successfully!")
        st.write(features)

# Button to call the gen_report_sr function
if st.button("Generate Report"):
    with st.spinner("Generating report..."):
        report = gen_report_sr()
        st.success("Report generated successfully!")
        st.write(report)

# Button to download the report
        st.download_button("Download Report", data="Report\SR_ADG_CYCLE.xlsx", file_name="SR_ADG_CYCLE.xlsx")

# Add text at the bottom of the page
st.write("Made with ❤️ by kevin")
