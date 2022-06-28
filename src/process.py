import logging
import pandas as pd
from hydra.utils import to_absolute_path as abspath
from sklearn.compose import ColumnTransformer
from os.path import exists

import hydra
from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath

from pipeline import num_pipe, cat_pipe
from utils import logger, log_time

from dwh import Features, Session, engine



def process_data(config):
    """Function to process the data
    Requires configuration file
    """
    local_session = Session(bind=engine)
    #assert "target_feature" in config.process, "config must contain target column"
    assert "cat_features" in config.process, "config must contain list of categorical columns"

    raw_path = abspath(config.raw.path)
    columns = config.process

    
    logger.info(f"Process data using {raw_path}")

    file_exists = exists(raw_path)
    if not file_exists:
        logger.error(f"{raw_path} does not exist")
        raise FileNotFoundError()

    data = pd.read_csv(raw_path, sep=' ', header=None)

    sensor_headers = [f'sensor_{x}' for x in range(1, 24)]
    # Combine column headers
    column_headers = columns.cat_features + sensor_headers

    # Assign the headers
    data.columns = column_headers
    # Separate in X and y
    sel_target = local_session.query(Features).filter(Features.targfeat==1).first() # use selected target feature via UI
    X = data.drop(sel_target.name, axis=1) # delete selected target feature via UI
    y = data[sel_target.name] # use selected target feature via UI
    
    # add column names (features) to data warehouse for UI


    # user input variables
    num_features = [col for col in X.columns if col not in columns.cat_features]
    cat_features = [col for col in columns.cat_features]

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', cat_pipe, cat_features),
            ('num', num_pipe, num_features)
        ]
    )

    X_processed = preprocessor.fit_transform(X)
    X_processed_df = pd.DataFrame(X_processed,columns=X.columns[:25])
    df = pd.concat([X_processed_df, y], axis=1)

    logger.info("Data successfully processed")

    return df
    

@hydra.main(version_base=None, config_path="../config", config_name='main')
def run(config: DictConfig): 
    processed_data = abspath(config.processed.path)
    df = process_data(
        config
    )
    
    df.to_feather(processed_data) # write preprocessed input dataframe for modelling later
    logger.info(f"Processed data saved to {processed_data}")

    return df


if __name__ == "__main__":
    run()
