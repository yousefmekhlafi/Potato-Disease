from pathlib import Path
from PotatoDisease.constants import *
from PotatoDisease.utils.common import read_yaml, create_directories
from PotatoDisease.entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([
            config.root_dir,
            config.unzip_train_dir,
            config.unzip_val_dir,
            config.unzip_test_dir
        ])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            train_data_source_URL=config.train_data_source_URL,
            val_data_source_URL=config.val_data_source_URL,
            test_data_source_URL=config.test_data_source_URL,
            local_train_data_file=config.local_train_data_file,
            local_val_data_file=config.local_val_data_file,
            local_test_data_file=config.local_test_data_file,
            unzip_train_dir=config.unzip_train_dir,
            unzip_val_dir=config.unzip_val_dir,
            unzip_test_dir=config.unzip_test_dir
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        return DataValidationConfig(
        image_dir=Path(config.image_dir),
        labels=config.labels,
        batch_size=config.batch_size,
        findings_output_file=Path(config.findings_output_file)
        )
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        return DataTransformationConfig(
            transformed_dir=Path(config.transformed_dir),
            unzip_train_dir=Path(config.unzip_train_dir),
            unzip_val_dir=Path(config.unzip_val_dir),
            unzip_test_dir=Path(config.unzip_test_dir)
        )