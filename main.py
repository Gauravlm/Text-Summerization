from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerpipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationpipeline

STAGE_NAME= 'Data Ingestion Stage'

try:
    logger.info(f'----- Stage {STAGE_NAME} started -----')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'----- Stage {STAGE_NAME} completed -----')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= 'Data Validation Stage'

try:
    logger.info(f'----- Stage {STAGE_NAME} started -----')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'----- Stage {STAGE_NAME} completed -----')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Tranformation Stage'
try:
    logger.info(f'----- Stage {STAGE_NAME} started -----')
    data_tranformation = DataTransformationPipeline()
    data_tranformation.main()
    logger.info(f'----- Stage {STAGE_NAME} completed -----')
except Exception as e:
    logger.exception(e)
    raise e
  
STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f'----- Stage {STAGE_NAME} started -----')
    model_trainer = ModelTrainerpipeline()
    model_trainer.main()
    logger.info(f'----- Stage {STAGE_NAME} completed -----')
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME = 'Model Evaluation Stage'
try:
    logger.info(f'----- Stage {STAGE_NAME} started -----')
    model_evaluation= ModelEvaluationpipeline()
    model_evaluation.main()
    logger.info(f'----- Stage {STAGE_NAME} completed -----')
except Exception as e:
    logger.exception(e)
    raise e 