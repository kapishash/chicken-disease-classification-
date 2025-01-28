from src.disease_classification import logger
from src.disease_classification import logger
from src.disease_classification.pipeline.data_ingestion import DataIngestionTrainingPipeline
# from disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
# from disease_classification.pipeline.stage_03_model_trainer import ModelTrainingPipeline
# from disease_classification.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e