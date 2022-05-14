
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv('./data/raw/train_FD001.txt', sep=' ', header=None)


class FeatureSelector:
    '''This class selects the categorical features or the numerical features of the data set. 

    Prameters
    ----------
    use_numbers: bool (default: True)
        select True if numerical features, or False if categorical features
    '''
    def __init__(self, use_numbers=True):
        assert type(use_numbers)==bool, "use_numbers must be of type bool"
        self.use_numbers = use_numbers
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        assert type(X)==pd.DataFrame, "X must be of type pandas.DataFrame"
        if self.use_numbers:
            return X.select_dtypes(include="number")
        else:
            return X.select_dtypes(exclude="number")
    
    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X, y)

class RemoveColumn:
    ''' This class evaluates all columns separately if the whole column consists missing values and removes the whole column.'''

    def __init__(self):
        #assert type(self)==pd.DataFrame, "DataFrame must be of type pandas.DataFrame"
        #self.use_numbers = use_numbers
        return None
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        assert type(X)==pd.DataFrame, "X must be of type pandas.DataFrame"
        for i in range(0,len(X.columns)):
            if X.iloc[:,i].isna().unique() == 'True':
                X.drop(i,axis=1, inplace=True)  # delete whole column
        return X
    
    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X, y)


# Separate in X and y
data.drop(np.arange(5), axis=1, inplace=True) # drop first 5 features, as they are categorical but stored as numerical
SEL_OUTPUT = 5  # user can put the selected index, which feature should be used as output variable
X = data.drop(SEL_OUTPUT, axis=1)
y = data.iloc[:,SEL_OUTPUT]

cat_pipe = Pipeline(steps=[
    ("selector", FeatureSelector(use_numbers=False)),
    ('remove', RemoveColumn()),
    ("impute", SimpleImputer(strategy="constant", fill_value="unknown")),
])

num_pipe = Pipeline(steps=[
    ("selector", FeatureSelector(use_numbers=True)),
    ('remove', RemoveColumn()),
    ("impute", SimpleImputer(strategy="constant", fill_value=0)),
    ("scaling", MinMaxScaler())
])

union = FeatureUnion(transformer_list=[
    ("num_pipe", num_pipe),
    ("non_num_pipe", cat_pipe)
])


union.fit_transform(X)

# questions:
# what to do with the cycle time? 
