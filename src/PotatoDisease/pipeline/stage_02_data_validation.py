from PotatoDisease.config.configuration import ConfigurationManager
from PotatoDisease.components.data_validation import ImageDataValidator
from PotatoDisease.logging import logger


class DataValidationPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_data_validation_config()

    def main(self):
        validator = ImageDataValidator(self.config)
        validator.validate()