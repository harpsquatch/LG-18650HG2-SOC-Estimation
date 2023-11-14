from SOCEst.constants import *                                  #Constants stores filepaths of yaml files we have in the directory 
from SOCEst.utils.common import read_yaml, create_directories   #From common, common functionalities are being imported 
from SOCEst.entity.config_entity import DataIngestionConfig     #Dataingestion configuration is being imported from config file where the class structure has been defined. 
from SOCEst.entity.config_entity import DataTransformationConfig
from SOCEst.entity.config_entity import ModelTrainerConfig

# This class will be responsible for managing configuration files. It reads config.yaml and creates necessary necessary directories in the artifacts folder  
class ConfigurationManager:  
    
    #The constructor take yaml file paths as arguments. 
    def __init__(self, config_filepath = CONFIG_FILE_PATH, #Config.yaml path 
                       params_filepath = PARAMS_FILE_PATH, #Params.yaml path 
                       schema_filepath = SCHEMA_FILE_PATH  #Schema,yaml path
                ): 

        self.config = read_yaml(config_filepath) #Config.yaml file is being read 
        self.params = read_yaml(params_filepath) #Params.yaml file is being read 
        self.schema = read_yaml(schema_filepath) #Schema,yaml file is being read 


        create_directories([self.config.artifacts_root]) #artifacts_root = artifacts so new folder artifact is created with this

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion  #take the configuration

        create_directories([config.root_dir]) #Create the root_dir = artifacts/data_ingestion

        data_ingestion_config = DataIngestionConfig(     #Here the data ingestion class is being inititalised by passing the neccessary variables. 
            root_dir=config.root_dir,                    
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config                     
        #Now from yaml file, the parameters data_ingestion class is successfully created. Next this has to be used in src/data_ingestion
    
    def get_data_transformation_config(self) -> DataTransformationConfig: 
        config = self.config.data_transformation
        params = self.params.data_parameters
        
        create_directories([config.root_dir]) #Create the root_dir = artifacts/data_transformation 
        
        data_transformation_config = DataTransformationConfig(     #Here the data ingestion class is being inititalised by passing the neccessary variables. 
            root_dir=config.root_dir,     
            data_path=config.data_path,
            train_names = config.train_names,
            test_names = config.test_names,
            downsampling = params.downsampling,
            output_capacity = params.output_capacity,
            scale_test = params.scale_test,
            output_time = params.output_time,
            steps = params.steps            
        )
        
        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig: 
        config = self.config.model_trainer
        params = self.params.model_parameters
        
        create_directories([config.root_dir]) #Create the root_dir = artifacts/data_transformation 
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,     
            model_name=config.model_name,
            steps = params.steps,
            num_features = params.num_features,
            dense_out = params.dense_out,
            num_hidden_units_1 = params.num_hidden_units_1,
            patience = params.patience,
            epochs = params.epochs,
            max_tuner = params.max_tuner,
            batch_size = params.batch_size,
            validation_split = params.validation_split,
            numberOfLayers = params.numberOfLayers,
            numberOfLSTMLayers = params.numberOfLSTMLayers,
            maxUnits = params.maxUnits,
            maxLSTMunits = params.maxLSTMunits,
            stepLSTMunit = params.stepLSTMunit,
            stepUnit = params.stepUnit,     
            numberOfDenseLayers = params.numberOfDenseLayers,
            maxDenseUnits = params.maxDenseUnits,
            stepDenseUnit = params.stepDenseUnit,
            maxDropout = params.maxDropout,
            dropoutRateStep = params.dropoutRateStep,
            layer = params.layer, 
            objective_metric = params.objective_metric, 
            save_dir = config.save_dir, 
            experiment_name = config.experiment_name 
        )
        
        return model_trainer_config
