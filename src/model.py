import pandas as pd

from pycaret import regression as pyreg

import pipeline as pipe

data = pd.read_feather('./data/processed/data_prep.feather')
setup = pyreg.setup(
    data,
    target=pipe.SEL_OUTPUT,
    numeric_features=pipe.SEL_NUM_FEATURES_PREP,
    categorical_features=pipe.SEL_CAT_FEATURES_PREP,
    normalize=False,
    data_split_shuffle = False,
    session_id=42,
    silent=True
)

model = pyreg.compare_models()
# pyreg.evaluate_model(model)

model_output = pyreg.pull()

# pyreg.evaluate_model(model)

print(model_output)