import sys
sys.path.append('./src')

import src.process as process
import src.model as model
import streamlit as st


def run():
    
    process.run()
    model.run()

if __name__ == "__main__":
    run()