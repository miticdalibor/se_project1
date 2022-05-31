import pandas as pd
from pycaret import regression as pyreg
from os.path import exists

import hydra
from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath

import pipeline as pipe
from src.utils import logger, log_time


@log_time
def train_models(path_to_file):
    """Training pycaret regression models"""
    file_exists = exists(path_to_file)

    if not file_exists:
        logger.error(f"{path_to_file} does not exist")
        raise FileNotFoundError()

    data = pd.read_feather(path_to_file)
    setup = pyreg.setup(
        data,
        target=pipe.SEL_OUTPUT,
        numeric_features=pipe.get_num_features(data),
        categorical_features=pipe.get_cat_features(data),
        normalize=False,
        data_split_shuffle = False,
        session_id=42,
        silent=True
    )

    model = pyreg.compare_models()
    logger.info("All Models trained")
    return model


@hydra.main(version_base=None, config_path="../config", config_name='main')
def run(config: DictConfig): 
    models_path = abspath(config.models.path)

    models = train_models(
        config.processed.path
    )

    models.to_pickle(models_path) # write preprocessed input dataframe for modelling later
    logger.info(f"All Models saved to {models_path}")
    return models


if __name__ == "__main__":
    run()
