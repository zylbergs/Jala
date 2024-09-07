import pandas as pd
import pickle
import streamlit as st

#use model to predict
#make below code into function
def predict_biomass(test_data, model):
    y_pred = model.predict(test_data)
    outcome = pd.DataFrame({'prediction result': y_pred})
    return outcome

