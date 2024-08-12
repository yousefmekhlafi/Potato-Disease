from PotatoDisease.config.configuration import ConfigurationManager
from PotatoDisease.components.data_transformation import DataTransformation
from PotatoDisease.logging import logger


class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_data_transformation_config()

    def main(self):
        try:
            logger.info("Starting the data transformation process...")
            data_transformation = DataTransformation(config=self.config)
            data_transformation.run()
            logger.info("Data transformation process completed successfully.")
        except Exception as e:
            logger.exception(f"Data transformation pipeline failed: {e}")