"""
import modules
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import time
import src

from src.dwh import Features, Session, engine

local_sesion = Session(bind=engine)
# import pycaret output

df = pd.read_feather('data/final/results.feather')

st.header('Get Predictions out of your Data')

# sidebar

data = st.sidebar.selectbox("Dataset: ",
					['Turbofan'])

# show all available features 
feat_list = []
features_dwh = local_sesion.query(Features).all() # query all features from dwh
for feat in features_dwh:
    feat_list.append(feat.name)   
features = st.sidebar.selectbox("Features in Dataset: ", feat_list)


# task definition
task = st.sidebar.radio("Task: ", ('Regression', 'Classification'))

if (task == 'Regression'):
    st.sidebar.success("Regression")
else:
    st.sidebar.success("Classification")

pred = st.sidebar.button("Latest training results!")

rtrain = st.sidebar.button("Retrain Dataset")


img = Image.open("pics/nodes.jpg")
st.image(img, width=750)

st.write("Your dataset is: ", data)

# Loading spinner

if pred:
    with st.spinner('Predicting...'):
        time.sleep(5)
st.success('Done!')

if pred:
    st.dataframe(df)

if rtrain:
    src.run()

