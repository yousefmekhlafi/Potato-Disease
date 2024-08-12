from PotatoDisease.logging import logger
from PotatoDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from PotatoDisease.pipeline.stage_02_data_validation import DataValidationPipeline
from PotatoDisease.pipeline.stage_03_data_transformation import DataTransformationPipeline 

# Define stage names
DATA_INGESTION_STAGE = "Data Ingestion Stage"
DATA_VALIDATION_STAGE = "Data Validation Stage"
DATA_TRANSFORMATION_STAGE = "Data Transformation Stage"  

try:
    # Data Ingestion Stage
    logger.info(f">>>>>> stage {DATA_INGESTION_STAGE} has started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {DATA_INGESTION_STAGE} completed <<<<<< \n\nx==========x")

    # Data Validation Stage
    logger.info(f">>>>>> stage {DATA_VALIDATION_STAGE} has started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {DATA_VALIDATION_STAGE} completed <<<<<< \n\nx==========x")

    # Data Transformation Stage
    logger.info(f">>>>>> stage {DATA_TRANSFORMATION_STAGE} has started <<<<<<")
    data_transformation = DataTransformationPipeline()  
    data_transformation.main()  
    logger.info(f">>>>>> stage {DATA_TRANSFORMATION_STAGE} completed <<<<<< \n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
