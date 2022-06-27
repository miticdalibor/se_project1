import sys
sys.path.append('./src')

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import sessionmaker
from datetime import datetime

location = 'sqlite:///dwh.db' # specify the database location
engine = create_engine(location, echo=True)

Base = declarative_base()
Session = sessionmaker()


class Features(Base):
    '''This class defines the metadata for the table generated for features.'''
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    catfeat = Column(Boolean)
    numfeat = Column(Boolean)
    targfeat = Column(Boolean)
    
    # the submethod is only needed for debugging to have a better representation
    def __repr__(self):
       return f"<Features(name={self.name}, catfeat={self.catfeat}, numfeat={self.numfeat}, targfeat={self.targfeat})>"

class PredResults(Base):
    '''This class defines the metadata for the table generated to store the results of the predictions'''
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime(), default=datetime.utcnow)
    index = Column(String)
    Model = Column(String)
    MAE = Column(Float)
    MSE = Column(Float)
    RMSE = Column(Float)
    R2 = Column(Float)
    RMSLE = Column(Float)
    MAPE = Column(Float)
    time_in_seconds = Column(Float)