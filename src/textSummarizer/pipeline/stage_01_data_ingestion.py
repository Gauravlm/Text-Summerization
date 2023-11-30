from textSummarizer.config.configuration import ConfigrationManager
from textSummarizer.conponents.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngestinoTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config= ConfigrationManager()
        data_ingestion_config= config.get_data_ingestion_config()
        data_ingestion= DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        