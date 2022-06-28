from threading import local
import pandas as pd
from pycaret import regression as pyreg
from os.path import exists

import hydra
from omegaconf import DictConfig
from hydra.utils import to_absolute_path as abspath

import pipeline as pipe
from utils import logger, log_time

from dwh import PredResults, Session, engine
# @todo: Fix column selection
@log_time
def train_models(config):
    """Training pycaret regression models"""

    assert "target_feature" in config.process, "config must contain target column"
    assert "cat_features" in config.process, "config must contain list of categorical columns"

    columns = config.process
    path_to_file = abspath(config.processed.path)

    file_exists = exists(path_to_file)

    if not file_exists:
        logger.error(f"{path_to_file} does not exist")
        raise FileNotFoundError()

    data = pd.read_feather(path_to_file)

    assert columns.target_feature in data.columns, "target column must be in dataframe columns"
    for col in columns.cat_features:
        assert col in data.columns, "categorical column must be in dataframe columns"

    num_features = [col for col in data.columns if col not in columns.cat_features + [columns.target_feature]]
    cat_features = [col for col in columns.cat_features]

    setup = pyreg.setup(
        data,
        target=columns.target_feature,
        numeric_features=num_features,
        categorical_features=cat_features,
        normalize=False,
        data_split_shuffle = False,
        session_id=42,
        silent=True
    )

    model = pyreg.compare_models()
    result = pyreg.pull()
    logger.info("All Models trained")

   

    return model, result


@hydra.main(version_base=None, config_path="../config", config_name='main')
def run(config: DictConfig):
    model_path = abspath(config.models.path)
    result_path = abspath(config.result.path)

    models, result = train_models(
        config
    )

    # models.to_pickle(model_path)
    # logger.info(f"All Models saved to {model_path}")
    result.reset_index().to_feather(result_path)
    logger.info(f"All Results saved to {result_path}")

     # add results to data warehouse
    local_session = Session(bind=engine)
    for i in range(0,len(result.reset_index())):
        new_result = PredResults(index=result.reset_index().loc[i,'index'],
                                Model=result.reset_index().loc[i,'Model'],
                                MAE=result.reset_index().loc[i,'MAE'],
                                MSE=result.reset_index().loc[i,'MSE'],
                                RMSE=result.reset_index().loc[i,'RMSE'],
                                R2=result.reset_index().loc[i,'R2'],
                                RMSLE=result.reset_index().loc[i,'RMSLE'],
                                MAPE=result.reset_index().loc[i,'MAPE'],
                                time_in_seconds=result.reset_index().loc[i,'TT (Sec)'])
        local_session.add(new_result)
        local_session.commit()
        logger.info(f"Row {i} added to data warehouse")
    logger.info("All Results saved to Data Warehouse")

    return result


if __name__ == "__main__":
    run()
