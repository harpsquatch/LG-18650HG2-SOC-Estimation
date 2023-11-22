from SOCEst import logger
from SOCEst.pipeline.stage1 import DataIngestionTrainingPipeline
from SOCEst.pipeline.stage2 import DataTransformationTrainingPipeline
from SOCEst.pipeline.stage3 import ModelTrainingPipeline
from SOCEst.pipeline.stage4 import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    stage2 = DataTransformationTrainingPipeline()
    train_x, train_y, test_x, test_y = stage2.main()
    #obj.combine_and_save_data(train_x, train_y, test_x, test_y)
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    stage3 = ModelTrainingPipeline(train_x, train_y)
    stage3.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    stage4 = ModelEvaluationTrainingPipeline(test_x, test_y)
    stage4.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e






