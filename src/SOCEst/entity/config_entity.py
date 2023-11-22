from dataclasses import dataclass
from pathlib import Path
from typing import List  # Add this import

@dataclass(frozen=True)   #This is a decorator
class DataIngestionConfig:
    root_dir: Path 
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#The above class takes rootdir, source_url, local_data_file, and unzip_dir as the variables. This we will get from config.yaml and then it will be used in the configuration.py file.

@dataclass(frozen=True)   #This is a decorator
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path
    train_names: List[str]
    test_names: List[str]
    downsampling: bool
    output_capacity: bool
    scale_test: bool
    output_time: bool
    steps: int
    
@dataclass(frozen=True)   #This is a decorator
class ModelTrainerConfig:
    root_dir: Path 
    #model_name: str
    steps: int
    num_features: int
    dense_out: int
    num_hidden_units_1: int
    patience: int
    epochs: int
    max_tuner: int
    batch_size: int
    validation_split: int
    numberOfLayers: int
    numberOfLSTMLayers: int
    maxUnits: int
    maxLSTMunits: int
    stepLSTMunit: int
    stepUnit: int
    numberOfDenseLayers: int
    maxDenseUnits: int
    stepDenseUnit: int
    maxDropout: int
    dropoutRateStep: int
    layer: str
    objective_metric: str
    #save_dir: Path
    experiment_name: str
    
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    mlflow_uri: str
    














    """
    The above lines of code helps us with, 
    
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand
    """