from SOCEst.config.configuration import ConfigurationManager
from SOCEst.components.data_transformation import DataTransformation 
from SOCEst import logger
import pandas as pd
import os

STAGE_NAME = "Data Transfromation stage"


#This pipeline decides which functions to use from the data_ingestion class and the same will be performed in the main file. 
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        cycles = data_transformation.get_discharge_whole_cycle()

        train_x, train_y, test_x, test_y = data_transformation.get_discharge_multiple_step(cycles)
        train_y = data_transformation.keep_only_y_end(train_y)
        test_y = data_transformation.keep_only_y_end(test_y)
        
        #self.train_test_save(train_x, train_y, test_x, test_y)
        flat_arrays = [arr.flatten() for arr in train_x]
        df = pd.DataFrame(flat_arrays)
  
        df.to_csv("D://New folder (2)//df3.csv", index=False)
        
        #self.train_test_save(train_x, train_y, test_x, test_y)
        flat_arrays = [arr.flatten() for arr in train_y]
        df1 = pd.DataFrame(flat_arrays)
  
        df1.to_csv("D://New folder (2)//df1.csv", index=False)

        return train_x, train_y, test_x, test_y
    
    def train_test_save(self, train_x, train_y, test_x, test_y):
        # Save train_x and train_y to CSV
        pd.DataFrame(train_x).to_csv(os.path.join(self.config.root_dir, "train_x.csv"), index=False)
        pd.DataFrame(train_y).to_csv(os.path.join(self.config.root_dir, "train_y.csv"), index=False)

        # Save test_x and test_y to CSV
        pd.DataFrame(test_x).to_csv(os.path.join(self.config.root_dir, "test_x.csv"), index=False)
        pd.DataFrame(test_y).to_csv(os.path.join(self.config.root_dir, "test_y.csv"), index=False)

        logger.info("Training and test sets are saved.")

        
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        train_x, train_y, test_x, test_y = obj.main()
        #obj.combine_and_save_data(train_x, train_y, test_x, test_y)
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

