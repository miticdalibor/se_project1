"""Source code of your project"""

import pandas as pd

import hydra
from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath

from process import process_data

@hydra.main(version_base=None, config_path="../config", config_name='main')
def run(config: DictConfig): 
    processed_input = abspath(config.processed.input_path)
    processed_output = abspath(config.processed.output_path)

    X, y = process_data(
        config.raw.path, 
        config.process.cat_index, 
        config.process.target_index
    )

    X.to_csv(processed_input) # write preprocessed input dataframe for modelling later
    y.to_csv(processed_output) # write output dataframe for modelling later

    return X, y

if __name__ == "__main__":
    run()