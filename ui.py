"""
import modules
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.header('Get Predictions out of your Data')

img = Image.open("pics/nodes.jpg")
st.image(img, width=750)

# Selection box

# first argument takes the title of the selectionbox
# second argument takes options
data = st.sidebar.selectbox("Dataset: ",
					['Turbofan'])

# print the selected hobby
st.write("Your dataset is: ", data)

# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button
task = st.sidebar.radio("Task: ", ('Regression', 'Classification'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (task == 'Regression'):
    st.sidebar.success("Regression")
else:
    st.sidebar.success("Classification")


# Create a simple button that does nothing
st.sidebar.button("Get Prediction")

# Create a button, that when clicked, shows a text
if(st.sidebar.button("About")):
	st.sidebar.text("WIP")







# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
