# LG-18650HG2-SOC-Estimation

Welcome to the LG-18650HG2 Battery SOC Estimation repository! This project aims to estimate the State of Charge (SOC) of LG-18650HG2 batteries using Bayesian Optimization and Neural Network models.

## Introduction

In the realm of energy storage systems, accurate SOC estimation is crucial for effective battery management. This repository explores the application of Bayesian Optimization and Neural Network techniques to estimate the SOC of LG-18650HG2 batteries.

## Data Source

The dataset used in this project is the LG-18650HG2 dataset. The dataset contains tests which were performed at McMaster University in Hamilton, Ontario, Canada by Dr. Phillip Kollmeyer (phillip.kollmeyer@gmail.com). A brand new 3Ah LG HG2 cell was tested in an 8 cu.ft. thermal chamber with a 75amp, 5 volt Digatron Firing Circuits Universal Battery Tester channel with a voltage and current accuracy of 0.1% of full scale. 

## Project Structure

The project is structured into the following components:

1. **Data Ingestion:**
- The Data Ingestion module is designed for the SOC (State of Charge) Estimation project. The DataIngestion class, initialized with a DataIngestionConfig object, facilitates the download and extraction of the dataset. Key methods include download_file() which downloads the dataset from a specified URL if not locally available and provides information about the download status. extract_zip_file() which extracts the contents of the downloaded zip file to a designated directory and Logs the creation of the unzip directory and extraction process.

2. **Data Transformation:**
- The DataTransformation module serves a crucial role in the broader battery state-of-charge (SoC) estimation pipeline by applying diverse transformations to battery discharge datasets. It encompasses several key functionalities: The first feature, Discharge Whole Cycle Extraction, is achieved through the get_discharge_whole_cycle() method, which isolates pertinent features and labels from the supplied datasets. This method outputs both training and testing sets. The Stateful Cycle Transformation functionality, implemented in the get_stateful_cycle(cycles, pad_num=0, steps=100) method, converts input cycles into stateful sequences. This involves padding sequences, splitting them into fixed steps, and delivering the transformed datasets. For the Multiple Step Discharge Transformation, the get_discharge_multiple_step(cycles) method breaks down input cycles into multiple steps, creating sequences suitable for training and testing. The resulting datasets include both training and testing sets. Data scaling is handled by the _scale_x(train, test, scale_test=False) method, ensuring that the input data within each feature is scaled to the [0, 1] range. This guarantees uniform scaling across training and testing datasets. The _time_string_to_seconds(input_string) method is dedicated to converting time strings to seconds, enhancing the representation of time-related data. Padded cycle transformation is facilitated by the _to_padded_cycle(cycles, pad_num, max_length) and _split_cycle(cycles, steps) methods, which respectively pad and split cycles into sequences for subsequent training and testing. Lastly, the keep_only_y_end(y, is_stateful=False) method retains only the end labels of input sequences.

4. **Model Training:**
- The "Model Training Stage" encompasses two hyperparameter optimization classes (modelHO_New and modelHO_SEGAN_LSTM) and the ModelTrainer class, facilitating the training of LSTM-based models for accurate State of Charge (SoC) estimation.modelHO_New Class: Utilizes Bayesian Optimization to fine-tune hyperparameters for LSTM-based SoC estimation models, including LSTM layer configuration, learning rate, and activation function.modelHO_SEGAN_LSTM Class: Similar to modelHO_New but tailored for a different model architecture—SEGAN LSTM. It optimizes hyperparameters such as LSTM layers, dense layers, dropout rates, and learning rates.ModelTrainer Class: Orchestrates the training process, leveraging the Bayesian Optimization tuner to search for optimal hyperparameters. It includes early stopping and model checkpointing for efficiency. Methods are provided to tune models and check tuner results. These components collectively enable the training of advanced models, enhancing the accuracy of SoC estimation through automated hyperparameter optimization.

4. **Model Evaluation:**
- The "Model Evaluation" component assesses the performance of a trained model using various metrics, including Root Mean Squared Error (RMSE) and Mean Squared Error (MSE). The evaluation is conducted on a test dataset, and the results are logged into MLflow for tracking.

5. **Model Deployment:**
- Currently working on this module. 

## Getting Started with the Project 

To get started with this project, follow the instructions below:

1. Clone the repository
2. Install the dependencies from requirements.txt
3. Change the configuration in YAML files present for different experiments
4. Run the main.py

## Contributing Guidelines:

We welcome contributions from the community to enhance the LG-18650HG2 Battery SOC Estimation project. If you're interested in contributing, please follow these guidelines:
- Fork the Repository
- Create a New Branch
- Make Changes, commit and make the request

## Issue Reporting
If you encounter any issues, have questions, or want to suggest improvements, please consider creating an issue. When creating an issue, provide detailed information about the problem and steps to reproduce it.

## Acknowledgments:
Description: Tests were performed at McMaster University in Hamilton, Ontario, Canada by Dr. Phillip Kollmeyer (phillip.kollmeyer@gmail.com). Reference: https://data.mendeley.com/datasets/cp3473x7xv/3
The project is developed in association with MG2 Lab, Politecnico di Milano

