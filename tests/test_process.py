import pandas as pd
import pytest

from src.process import process_data
from src.pipeline import RemoveColumn


def test_input_shape():
    """Test shape of input data"""
    res = process_data("data/raw/train_FD001.txt", 5, 8)
    assert res.shape == (20631,26)


def test_column_remove():
    """Test transformation using RemoveColumn class"""
    data = pd.read_csv("data/raw/train_FD001.txt", sep=' ', header=None)
    assert data.shape[1] == 28
    remover = RemoveColumn()
    data_removed = remover.fit_transform(data)
    assert data_removed.shape[1] == 26
    

def test_file_error():
    with pytest.raises(FileNotFoundError) as exc_info:   
        res = process_data("data/raw/file_not_there.txt", 5, 8)


def test_assert_cat_error():
    with pytest.raises(AssertionError) as exc_info:   
        res = process_data("data/raw/train_FD001.txt", "test", 8)
    assert str(exc_info.value) == "Category index must be of type int"