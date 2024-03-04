import streamlit as st
import numpy as np
import pandas as pd
import joblib


model = joblib.load('xgb_model.joblib');
st.tittle('How much Is this')