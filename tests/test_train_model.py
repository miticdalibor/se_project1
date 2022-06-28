import pytest
from hydra import initialize, compose

from src.model import train_models
from src.pipeline import RemoveColumn

def test_model_file_error():
    with pytest.raises(FileNotFoundError) as exc_info:
        with initialize(version_base=None, config_path="../config"):
            cfg = compose(config_name="main", overrides=["processed.path=column_not_exists"])
            res = train_models(cfg)


# @TODO: Check as target_feature does not exist in config
#def test_assert_target_error():
#    with pytest.raises(AssertionError) as exc_info:   
#        with initialize(version_base=None, config_path="../config"):
#            cfg = compose(config_name="main", overrides=["process.target_feature=column_not_exists"])
#            res = train_models(cfg)
#    assert str(exc_info.value) == "target column must be in dataframe columns"