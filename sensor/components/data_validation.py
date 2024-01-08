from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os, sys
import pandas as pd

class DataValidation:

    def __init__(self, data_validation_config: config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'* 20} Data Validation {'<<'* 20}")
            self.data_validation_config= data_validation_config
        except Exception as e:
            raise SensorException(e, sys)

    def is_required_columns_exists(self,)-> bool:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def drop_missing_values_columns(self, df: pd.DataFrame, threshold: float= 0.3)-> pd.DataFrame:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self)-> artifact_entity.DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)