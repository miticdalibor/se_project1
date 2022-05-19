import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

class RemoveColumn:
    ''' This class evaluates all columns separately.
    If the whole column consists missing values and removes the whole column.
    '''

    def __init__(self):
        return None

    def fit(self, X, y=None):
        '''Fit the Remover to input data'''
        return self

    def transform(self, X, y=None):
        '''Transform input data removing empty columns'''
        assert isinstance(X, pd.DataFrame), 'X must be of type pandas.DataFrame'

        for i in X.columns:
            if X[i].isna().all():
                X.drop(i,axis=1, inplace=True)  # delete whole column
        return X

    def fit_transform(self, X, y=None):
        '''Combination of fit and transform.
        Fits input data and returns a transformed dataframe'''
        self.fit(X, y)
        return self.transform(X, y)


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
