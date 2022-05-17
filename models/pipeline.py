
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


data = pd.read_csv('./data/raw/train_FD001.txt', sep=' ', header=None)

class RemoveColumn:
    ''' This class evaluates all columns separately if the whole column consists missing values and removes the whole column.'''

    def __init__(self):
        return None
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        assert type(X)==pd.DataFrame, 'X must be of type pandas.DataFrame'
        
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
    ('remove', RemoveColumn()),
    ('impute_cat', SimpleImputer(strategy='constant', fill_value=999)),
    ('encoder_cat', OrdinalEncoder()) # does not work well? 
    
])

num_pipe = Pipeline(steps=[
    ('remove', RemoveColumn()),
    ('impute_num', SimpleImputer(strategy='constant', fill_value=0)),
    ('scaling', MinMaxScaler())
])


# questions:
# what to do with the cycle time? 

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_pipe, SEL_NUM_FEATURES),
        ('cat', cat_pipe, SEL_CAT_FEATURES)
    ]
)

test = preprocessor.fit_transform(X)

o = pd.DataFrame(test,columns=X.columns[:25])
print(o)

r=OrdinalEncoder()
check = r.fit_transform(X[SEL_CAT_FEATURES].values)
print(check)