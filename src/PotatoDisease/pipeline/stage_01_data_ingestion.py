from PotatoDisease.config.configuration import ConfigurationManager
from PotatoDisease.components.data_ingestion import DataIngestion
from PotatoDisease.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()  # Initialize ConfigurationManager
        data_ingestion_config = config.get_data_ingestion_config()  # Access the configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Loop through the dataset types and perform download and extraction
        for dataset_type in ['train', 'val', 'test']:
            data_ingestion.download_file(dataset_type)
            data_ingestion.extract_zip_file(dataset_type) 