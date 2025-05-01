import pandas as pd 
import numpy as np
from src.exception import CustomException
from src.logger import logging
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv("C:/Users/PMYLS/Desktop/My Data/stock price/stock_data.csv")
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path))
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            train_df,test_df=train_test_split(df,test_size=0.2,random_state=42)
            train_df.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_df.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            return(
                train_df,
                test_df
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e,sys)