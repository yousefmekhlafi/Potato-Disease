import os
import cv2
import logging
import numpy as np
from pathlib import Path
from PotatoDisease.config.configuration import ConfigurationManager
from PotatoDisease.entity import DataTransformationConfig
from torchvision import transforms

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def resize_image(self, image, size=(256, 256)):
        """Resize the image to the given size."""
        return cv2.resize(image, size)

    def augment_image(self, image):
        """Apply augmentation techniques to the image."""
        transform = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(10),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1)
        ])
        image = transforms.ToPILImage()(image)
        augmented_image = transform(image)
        return np.array(augmented_image)

    def transform_images(self, input_dir: Path, output_dir: Path):
        """Transform images by resizing and augmenting."""
        os.makedirs(output_dir, exist_ok=True)
        for root, _, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                image = cv2.imread(file_path)
                if image is None:
                    self.logger.warning(f"Could not read image: {file_path}")
                    continue
                
                resized_image = self.resize_image(image)
                resized_image_path = os.path.join(output_dir, f"resized_{file}")
                cv2.imwrite(resized_image_path, resized_image)

                augmented_image = self.augment_image(resized_image)
                augmented_image_path = os.path.join(output_dir, f"augmented_{file}")
                cv2.imwrite(augmented_image_path, augmented_image)

    def run(self):
        try:
            self.logger.info("Starting data transformation...")

            # Process train images
            train_output_dir = os.path.join(self.config.transformed_dir, 'train')
            self.transform_images(self.config.unzip_train_dir, train_output_dir)

            # Process validation images
            val_output_dir = os.path.join(self.config.transformed_dir, 'val')
            self.transform_images(self.config.unzip_val_dir, val_output_dir)

            # Process test images
            test_output_dir = os.path.join(self.config.transformed_dir, 'test')
            self.transform_images(self.config.unzip_test_dir, test_output_dir)

            self.logger.info("Data transformation completed. Transformed images saved.")
        except Exception as e:
            self.logger.exception(e)