import pandas as pd
from src.process import process_data
from src.pipeline import RemoveColumn

def test_input_output():
    """Test if input and output are splitted"""
    res = process_data("data/raw/train_FD001.txt", 5, 8)
    print(res[0].shape)
    print(res[1].shape)
    assert len(res) == 2


def test_input_shape():
    """Test shape of input data"""
    res = process_data("data/raw/train_FD001.txt", 5, 8)
    assert res[0].shape == (20631,25)


def test_output_shape():
    """Test shape of output data"""
    res = process_data("data/raw/train_FD001.txt", 5, 8)
    assert res[1].shape == (20631,)


def test_column_remove():
    """Test transformation using RemoveColumn class"""
    data = pd.read_csv("data/raw/train_FD001.txt", sep=' ', header=None)
    assert data.shape[1] == 28
    remover = RemoveColumn()
    data_removed = remover.fit_transform(data)
    assert data_removed.shape[1] == 26
    