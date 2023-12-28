from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, data_ingesttion_config: config_entity.DataIngestionConfig):
        try:
            self.data_ingesttion_config= data_ingesttion_config
        except exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)-> artifact_entity.DataIngestionArtifact:
        try:
            #Exporting collection data as pandas dataframe 
            df: pd.DataFrame= utils.get_collection_as_dataframe(
                database_name= self.data_ingesttion_config.database_name, 
                collection_name= self.data_ingesttion_config.collection_name)

            #Replacing the null values with the mean
            df.replace(to_replace= "na", value= np.NAN, inplace= True)
            
        except exception as e:
            raise SensorException(e, sys)