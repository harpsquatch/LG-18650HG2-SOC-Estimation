from SOCEst.config.configuration import ConfigurationManager
from SOCEst.components.model_trainer import ModelTrainer 
from SOCEst.components.model_trainer import modelHO_New
from SOCEst.components.model_trainer import modelHO_SEGAN_LSTM
from SOCEst.pipeline.stage2 import DataTransformationTrainingPipeline
from SOCEst import logger
import pandas as pd
import os


STAGE_NAME = "Model Training Stage"
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        data_pipeline = DataTransformationTrainingPipeline()
        train_x, train_y, test_x, test_y = data_pipeline.main()
        
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model, history = model_trainer.tune_modelClass(train_x, train_y)
        model.summary()
        model.save(model_trainer.directory + '/models')
        print("Model has been trainer and is saved in the location specified")
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        

