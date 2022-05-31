import pytest

from src.model import train_models
from src.pipeline import RemoveColumn

def test_model_file_error():
    with pytest.raises(FileNotFoundError) as exc_info:   
        res = train_models("data/processed/file_not_there.feather")