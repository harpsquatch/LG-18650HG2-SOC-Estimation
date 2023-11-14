import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from SOCEst.entity.config_entity import ModelEvaluationConfig
from SOCEst.utils.common import save_json
from pathlib import Path
#import get_flops
import h5py
import math
from tensorflow.keras.models import load_model

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,model,actual, pred):
        rmse = math.sqrt(np.mean(np.square(np.subtract(pred, actual))))/np.mean(actual) 
        mse = np.mean(np.mean(np.square(np.subtract(pred, actual))))
        #flops = get_flops(model, batch_size=64)
        
        return rmse, mse
    

    def log_into_mlflow(self,test_x,test_y):
        
        with h5py.File(self.config.model_path, 'r') as file:
            model = load_model(file)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_SOC = model.predict(test_x)

            (rmse, mse) = self.eval_metrics(model, test_y, predicted_SOC)
            
            # Saving metrics as local
            scores = {"rmse": rmse,"mse":mse } #,  "flops":flops
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mse", mse)
           # mlflow.log_metric("flops", mae)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="BiLSTM Bayesian Optmized")
            else:
                mlflow.sklearn.log_model(model, "model")

    
