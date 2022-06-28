"""
import modules
"""
import sys
sys.path.append('./src')
import streamlit as st
import pandas as pd
from PIL import Image

import time
import src

from src.dwh import Features, Session, engine
from sqlalchemy import insert, update
import src.dwh_init 

local_session = Session(bind=engine) # create local session for accessing the dB
x = 0

df = pd.read_feather('data/final/results.feather')

st.header('Get Predictions out of your Data')

# sidebar

data = st.sidebar.selectbox("Dataset: ",
					['Turbofan'])

# show all available features
feat_list = []
features_dwh = local_session.query(Features).all() # query all features from dwh
for feat in features_dwh:
    feat_list.append(feat.name)
target_feature = st.sidebar.selectbox("Select your Target Feature: ", feat_list)

if target_feature:
    x+=1
    local_session.query(Features).update({'targfeat':0}) # set all values to 0, as only one target feature is possible
    local_session.commit()
    local_session.query(Features).filter(Features.name==target_feature).update({'targfeat':1}) # set selected target feature to 1 for backend
    local_session.commit()


# task definition
task = st.sidebar.radio("Task: ", ('Regression', 'Classification'))

if (task == 'Regression'):
    x+=1
    st.sidebar.success("Regression")
else:
    x+=1
    st.sidebar.success("Classification")

pred = st.sidebar.button("Latest training results!")

rtrain = st.sidebar.button("Retrain Dataset")


img = Image.open("pics/nodes.jpg")
st.image(img, width=750)

st.write("Your dataset is: ", data)

# Loading spinner

if pred:
    x+=1
    #with st.spinner('Predicting...'):
    #    time.sleep(5)
    st.dataframe(df)
    st.success('Done!')

if rtrain:
    x+=1
    src.run()
    st.success('Done!')

if x == 0:
    src.dwh_init.run() # only initialize DB when application starts
