from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    train_data_source_URL: str
    val_data_source_URL: str
    test_data_source_URL: str
    local_train_data_file: Path
    local_val_data_file: Path
    local_test_data_file: Path
    unzip_train_dir: Path
    unzip_val_dir: Path
    unzip_test_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    image_dir: Path
    labels: list
    batch_size: int
    findings_output_file: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    transformed_dir: Path
    unzip_train_dir: Path
    unzip_val_dir: Path
    unzip_test_dir: Path