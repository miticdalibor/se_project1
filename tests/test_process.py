import pandas as pd
import pytest
from hydra import initialize, compose


from src.process import process_data
from src.pipeline import RemoveColumn


def test_input_shape():
    """Test shape of input data"""
    with initialize(version_base=None, config_path="../config"):
        # config is relative to a module
        cfg = compose(config_name="main")
        res = process_data(cfg)
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
        with initialize(version_base=None, config_path="../config"):
            # config is relative to a module
            cfg = compose(config_name="main", overrides=["raw.path=file_not_exists.txt"])
            res = process_data(cfg)