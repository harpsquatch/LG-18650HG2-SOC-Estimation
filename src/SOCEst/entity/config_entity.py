from dataclasses import dataclass
from pathlib import Path


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















    """
    The above lines of code helps us with, 
    
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand
    """