import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer

data = pd.read_csv('./data/raw/train_FD001.txt', sep=' ', header=None)

class RemoveColumn:
    ''' This class evaluates all columns separately if the whole column consists 
    missing values and removes the whole column.'''

    def __init__(self):
        return None

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        assert type(X) == pd.DataFrame, 'X must be of type pandas.DataFrame'

        for i in X.columns:          
            if X[i].isna().all() == True:
                X.drop(i,axis=1, inplace=True)  # delete whole column
        return X

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X, y)

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
all_headers = column_headers + ['rul']

# Assign the headers
data.columns = column_headers

print(data.columns)
# user output variable
SEL_OUTPUT = data.columns[8]  # user can put the selected feature as output variable

# Separate in X and y
X = data.drop(SEL_OUTPUT, axis=1)
y = data[SEL_OUTPUT]

# user input variables
SEL_CAT_FEATURES = X.columns[:5].values # user can put the selected categorical features 
SEL_NUM_FEATURES = X.columns[5:].values # user can put the selected numerical features 
ALL_FEATURES = X.columns.values



cat_pipe = Pipeline(steps=[
    ('remove_cat', RemoveColumn()),
    ('impute_cat', SimpleImputer(strategy='constant', fill_value=999)),
    ('encoder_cat', OrdinalEncoder()) # does not work well? 
    
])

num_pipe = Pipeline(steps=[
    ('remove_num', RemoveColumn()),
    ('impute_num', SimpleImputer(strategy='constant', fill_value=0)),
    ('scaling', MinMaxScaler())
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', cat_pipe, SEL_CAT_FEATURES),
        ('num', num_pipe, SEL_NUM_FEATURES)
    ]
)

X_prep = preprocessor.fit_transform(X)
X_prep_df = pd.DataFrame(X_prep,columns=X.columns[:25])
data_prep_df = pd.concat([X_prep_df, y], axis=1)
data_prep_df.to_feather('./data/processed/data_prep.feather') # write preprocessed input dataframe for modelling later
#y.to_feather('./data/processed/Output_prep1.feather') # write output dataframe for modelling later

# adapt features after preprocessing
SEL_NUM_FEATURES_PREP = []
SEL_CAT_FEATURES_PREP = []
for i in SEL_NUM_FEATURES:
    if i in X_prep_df.columns:
        SEL_NUM_FEATURES_PREP.append(i)

for i in SEL_CAT_FEATURES:
    if i in X_prep_df.columns:
        SEL_CAT_FEATURES_PREP.append(i)
