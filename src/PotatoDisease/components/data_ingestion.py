import os
import urllib.request as request
import zipfile
from PotatoDisease.logging import logger
from PotatoDisease.utils.common import get_size
from tqdm import tqdm
from pathlib import Path
from PotatoDisease.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self, dataset_type):
        if dataset_type == "train":
            url = self.config.train_data_source_URL
            local_data_file = self.config.local_train_data_file
        elif dataset_type == "val":
            url = self.config.val_data_source_URL
            local_data_file = self.config.local_val_data_file
        elif dataset_type == "test":
            url = self.config.test_data_source_URL
            local_data_file = self.config.local_test_data_file
        else:
            raise ValueError("Invalid dataset type. Choose from 'train', 'val', or 'test'.")

        logger.info(f"Downloading {dataset_type} dataset from {url}...")
        request.urlretrieve(url, local_data_file)
        logger.info(f"Downloaded {dataset_type} dataset to {local_data_file}.")

    def extract_zip_file(self, dataset_type):
        if dataset_type == "train":
            local_data_file = self.config.local_train_data_file
            unzip_path = self.config.unzip_train_dir
        elif dataset_type == "val":
            local_data_file = self.config.local_val_data_file
            unzip_path = self.config.unzip_val_dir
        elif dataset_type == "test":
            local_data_file = self.config.local_test_data_file
            unzip_path = self.config.unzip_test_dir
        else:
            raise ValueError("Invalid dataset type. Choose from 'train', 'val', or 'test'.")

        os.makedirs(unzip_path, exist_ok=True)
        
        # Verify the zip file before extracting
        if zipfile.is_zipfile(local_data_file):
            logger.info(f"Extracting {dataset_type} dataset...")
            with zipfile.ZipFile(local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted {dataset_type} dataset to {unzip_path}.")
        else:
            raise zipfile.BadZipFile("The file is not a valid zip file.")