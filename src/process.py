import pandas as pd
from hydra.utils import to_absolute_path as abspath
from sklearn.compose import ColumnTransformer
from os.path import exists

import hydra
from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath

from pipeline import num_pipe, cat_pipe
from src.utils import logger, log_time

def process_data(raw_path, cat_idx, target_idx):
    """Function to process the data
    Requires configuration file
    """

    assert isinstance(cat_idx, int), "Category index must be of type int"
    assert isinstance(target_idx, int), "Target index must be of type int"

    raw_path = abspath(raw_path)
    
    logger.info("Process data using {raw_path}")

    file_exists = exists(raw_path)
    if not file_exists:
        logger.error("{path_to_file} does not exist")
        raise FileNotFoundError()

    data = pd.read_csv(raw_path, sep=' ', header=None)

    # Define column headers, as the data should have column names
    preamble_headers = [
        'unit_number',
        'cycles',
        'operational_setting_1',
        'operational_setting_2',
        'operational_setting_3'
    ]
    sensor_headers = [f'sensor_{x}' for x in range(1, 24)]
    # Combine column headers
    column_headers = preamble_headers + sensor_headers

    # Assign the headers
    data.columns = column_headers

    # user output variable
    SEL_OUTPUT = data.columns[target_idx]  # user can put the selected feature as output variable

    # Separate in X and y
    X = data.drop(SEL_OUTPUT, axis=1)
    y = data[SEL_OUTPUT]

    # user input variables
    SEL_CAT_FEATURES = X.columns[:cat_idx].values # user can put the selected categorical features 
    SEL_NUM_FEATURES = X.columns[cat_idx:].values # user can put the selected numerical features

    # questions: 
    # what to do with the cycle time?
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', cat_pipe, SEL_CAT_FEATURES),
            ('num', num_pipe, SEL_NUM_FEATURES)
        ]
    )

    X_processed = preprocessor.fit_transform(X)
    X_processed_df = pd.DataFrame(X_processed,columns=X.columns[:25])
    df = pd.concat([X_processed_df, y], axis=1)
    
    return df
    

@hydra.main(version_base=None, config_path="../config", config_name='main')
def run(config: DictConfig): 
    processed_data = abspath(config.processed.path)

    df = process_data(
        config.raw.path,
        config.process.cat_index,
        config.process.target_index
    )

    df.to_feather(processed_data) # write preprocessed input dataframe for modelling later

    return df

if __name__ == "__main__":
    run()
