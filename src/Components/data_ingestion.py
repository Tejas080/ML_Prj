##Reading data from specific location that is your data ingestion

import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass ## used in creating class variable

##when ever we are performing data ingestion component there are some inputs required for it.
## like where we have save train data test data and raw data this kind of inputs we have to using class.

##inside class we use init to define variable
## but if you decorator it will directly define your variable


## all train data stored in artifact folder

@dataclass

class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")

class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion metohd or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')  #reading data set form anywhere
            logging.info('Read dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)  

            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df,test_size=0.20,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)

            logging.info("Ingestion of data completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = Dataingestion()
    obj.initiate_data_ingestion()

