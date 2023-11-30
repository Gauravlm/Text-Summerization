from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestinoTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME= 'Data Ingestion Stage'

try:
    logger.info(f'----- Stage {STAGE_NAME} started -----')
    data_ingestion = DataIngestinoTrainingPipeline()
    data_ingestion.main()
    logger.info(f'----- Stage {STAGE_NAME} completed -----')
except Exception as e:
    logger.exception(e)
    raise e

