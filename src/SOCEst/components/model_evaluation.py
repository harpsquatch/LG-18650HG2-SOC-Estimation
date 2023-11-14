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
from keras_flops import get_flops


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,model,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        mse = np.mean(np.mean(np.square(np.subtract(pred, actual))))
        r2 = r2_score(actual, pred)
        flops = get_flops(model, batch_size=64)
        
        return rmse, mae, mse, r2, flops
    

    def log_into_mlflow(self,test_x,test_y):

        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_SOC = model.predict(test_x)

            (rmse, mae, mse, r2, flops) = self.eval_metrics(test_y, predicted_SOC)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2 ,"mse":mse,  "flops":flops }
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("mse", mae)
            mlflow.log_metric("flops", mae)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="BiLSTM Bayesian Optmized")
            else:
                mlflow.sklearn.log_model(model, "model")

    
