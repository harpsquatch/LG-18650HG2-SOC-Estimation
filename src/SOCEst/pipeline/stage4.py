from SOCEst.config.configuration import ConfigurationManager
from SOCEst.components.model_evaluation import ModelEvaluation
from SOCEst.pipeline.stage2 import DataTransformationTrainingPipeline
from SOCEst import logger
import os

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self, test_x, test_y):
        self.test_x = test_x
        self.test_y = test_y

    def main(self):
       # data_pipeline = DataTransformationTrainingPipeline()
       # train_x, train_y, test_x, test_y = data_pipeline.main()
        
        config = ConfigurationManager()
        experiment_name = config.config.model_trainer.experiment_name
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        
        experiment_path = os.path.join(model_evaluation_config.model_path, f"{experiment_name}.h5")
        
        model_evaluation.log_into_mlflow(experiment_path,self.test_x,self.test_y)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
