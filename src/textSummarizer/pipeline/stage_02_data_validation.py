from textSummarizer.config.configuration import ConfigrationManager
from textSummarizer.conponents.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config= ConfigrationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_file_exist()

        #
        