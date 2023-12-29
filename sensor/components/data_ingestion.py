from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config= data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)-> artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Exporting collection data as pandas dataframe")
            #Exporting collection data as pandas dataframe 
            df: pd.DataFrame= utils.get_collection_as_dataframe(
                database_name= self.data_ingestion_config.database_name, 
                collection_name= self.data_ingestion_config.collection_name)

            logging.info(f"Replacing the null values with the mean")
            #Replacing the null values with the mean
            df.replace(to_replace= "na", value= np.NAN, inplace= True)
            
            logging.info(f"Creating Feature Store Directory")
            #Creating Feature Store Directory
            feature_store_dir= os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok= True)

            logging.info(f"Saving df to feature store folder")
            #Saving df to feature store folder
            df.to_csv(path_or_buf= self.data_ingestion_config.feature_store_file_path)

            logging.info(f"Splitting dataset into train and test")
            #Splitting dataset into train and test
            #train_df, test_df= train_test_split(df, test_size= self.data_ingestion_config.test_size, random_state= 42)
            train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size,random_state=42)

            logging.info(f"Creating dataset directory")
            #Creating dataset directory
            dataset_dir= os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok= True)

            logging.info(f"Saving train and test file to dataset directory")
            #Saving train and test file to dataset directory
            train_df.to_csv(path_or_buf= self.data_ingestion_config.train_file_path)
            test_df.to_csv(path_or_buf= self.data_ingestion_config.test_file_path)

            logging.info(f"Preparing Artifact")
            #Preparing Artifact
            data_ingestion_artifact= artifact_entity.DataIngestionArtifact(
                feature_store_file_path= self.data_ingestion_config.feature_store_file_path,
                train_file_path= self.data_ingestion_config.train_file_path,
                test_file_path= self.data_ingestion_config.test_file_path
            )

            logging.info(f"Data Ingestion Completed")
            return(data_ingestion_artifact)

        except Exception as e:
            raise SensorException(e, sys)