from src.cnnClassifier import logger
<<<<<<< HEAD
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

#logger.info("Welcome to our custom log")


STAGE_NAME="Data Ingestion"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
=======


logger.info("Welcome to our custom log")
>>>>>>> cc9636832a0a63936319efee539e9c3ff59a403d
