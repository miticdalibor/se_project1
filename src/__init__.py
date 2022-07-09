import sys
sys.path.append('./src')

import src.process as process
import src.model as model
import streamlit as st

@st.cache(hash_funcs={"MyUnhashableClass": lambda _: None})
def run():
    
    process.run()
    model.run()

if __name__ == "__main__":
    run()