from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig)
import os

class ConfigrationManager:
    def __init__(self,
                 config_file_path= CONFIG_FILE_PATH,
                 params_file_path= PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params= read_yaml(params_file_path)

        if not os.path.exists(self.config.artifacts_root):
            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config= self.config.data_ingestion
        if not os.path.exists(config.root_dir):
            create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
            )
        return data_ingestion_config

