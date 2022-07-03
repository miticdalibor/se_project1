"""
import modules
"""
import sys
import timeit
from click import progressbar
sys.path.append('./src')
import streamlit as st
import pandas as pd
from PIL import Image
from stqdm import stqdm
from sklearn import metrics
import time
import src

from src.dwh import Features, Session, engine
from sqlalchemy import insert, update
import src.dwh_init 

local_session = Session(bind=engine) # create local session for accessing the dB
x = 0

st.set_page_config(
    page_title="Auto-ML Dashboard by Frunch Infinity",
    page_icon="✅",
    layout="wide",
)

df = pd.read_feather('data/final/results.feather')

st.header('Generate model output of your Data')

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
    st.sidebar.success("Classification is currently not available in our MVP Application")

pred = st.sidebar.button("Latest training results!")

rtrain = st.sidebar.button("Retrain Dataset")


#img = Image.open("pics/nodes.jpg")
#st.image(img, width=750)

#st.write("Your dataset is: ", data)

# Loading spinner

if pred:
    x+=1
    #with st.spinner('Predicting...'):
    #    time.sleep(5)
    st.dataframe(df)
    

if rtrain:
        with st.spinner("we hope you have brought some time :)"):
            for i in stqdm(range(0,1)):
                start_time = timeit.default_timer()
                src.run()
                elapsed = timeit.default_timer() - start_time
                st.success('Press "Latest Training Results" to see the training output')
         

if x == 0:
    src.dwh_init.run() # only initialize DB when application starts


#src.run()
