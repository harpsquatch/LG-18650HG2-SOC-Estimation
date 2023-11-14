# LG-18650HG2-SOC-Estimation


## Workflows

1. Update config.yaml  #This is for the user to change 
2. Update schema.yaml  # 
3. Update params.yaml  # 
4. Update the entity   # 
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


#Data Ingestion: 

config.yaml + config entity > Create Configuration > data_ingestion function > Pipeline > Main to run the pipeline 
config.yaml takes the parameters from users
config entity defines the configuration for the data_ingestion 
Then the above two are matched together to create the data_ingestion configuration 
Based on the above config, different fucntions are created in data ingestion files 
Based on the config files, selected funtions are perofomed from the data ingestion class 
Finally the pipline is run in the main file.



#Data Transformation: 





MLFLOW_TRACKING_URI=https://dagshub.com/harpreets924/LG-18650HG2-SOC-Estimation.mlflow \
MLFLOW_TRACKING_USERNAME=harpreets924 \
MLFLOW_TRACKING_PASSWORD=8eb72334d69388c2b0a5203d6cf274b6d877267a \
python script.py