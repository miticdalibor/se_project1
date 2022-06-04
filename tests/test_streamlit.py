"""
Streamlit integration test
prequesite local running streamlit
"""
import subprocess
import time
from urllib import response

import requests


def test_streamlit():
    url = "http://0.0.0.0:8501"
    proc = subprocess.Popen(["streamlit", "run", "ui.py"])
    time.sleep(10)
    try:
        test_response = requests.get(url)
        assert test_response.status_code == 200
    finally:
        proc.terminate()
    time.sleep(0.1)
