
from dwh import Features, PredResults, engine, Session
from utils import logger
from omegaconf import DictConfig
import hydra

@hydra.main(version_base=None, config_path="../config", config_name='main')
def run(config: DictConfig):
    '''Initialize Features and PredResults Table with the start of the application to have a clean DB.'''
    local_session = Session(bind=engine)
    local_session.query(Features).delete()
    local_session.query(PredResults).delete()
    local_session.commit()
    
    columns = config.process
    sensor_headers = [f'sensor_{x}' for x in range(1, 24)]
    column_headers = columns.cat_features + sensor_headers

    # add column names (features) to data warehouse for UI
    for i in column_headers[5:]:
        new_feature = Features(name=i)
        local_session.add(new_feature)
        local_session.commit()
        logger.info(f"Feature {i} added to DB.")
    
    logger.info("All Data in DB deleted and DB initialized.")


if __name__ == "__main__":
    run()