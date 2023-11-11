from SOCEst.config.configuration import ConfigurationManager
from SOCEst.components.data_transformation import DataTransformation 
from SOCEst import logger

STAGE_NAME = "Data Transfromation stage"


#This pipeline decides which functions to use from the data_ingestion class and the same will be performed in the main file. 
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def datasetnames(): 
        train_names = ['0degC/589_LA92']
        test_names =['0degC/589_Mixed1']
    
    def main(data_path, data_opt):
        
        train_names, test_names = datasetnames()
        data_transformation = DataTransformation(data_path)
        steps = data_opt['n_back']
        cycles = data_transformation.get_discharge_whole_cycle(train_names, test_names,downsampling=data_opt['downsampling'], output_capacity=False, scale_test=True)
        train_x, train_y, test_x, test_y = data_transformation.get_discharge_multiple_step(cycles, steps)
        train_y = data_transformation.keep_only_y_end(train_y, steps)
        test_y = data_transformation.keep_only_y_end(test_y, steps)

        return train_x, train_y, test_x, test_y
        
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

