# End-to-End Machine Learning Project

## Overview
This project demonstrates an end-to-end machine learning pipeline, from data collection to model deployment. The entire workflow is implemented using Python, and Streamlit is used for deploying the trained model.

## Project Structure
```
|-- Data
|   |-- Raw_Data
|   |   |-- Raw.csv
|   |-- Cleaned_Data
|   |   |-- Cleaned_Data.csv
|   |-- preprocess_Data
|   |   |-- preprocessed.csv
|   |   |-- preprocesses.csv
|   |   |-- X_train.csv
|   |   |-- X_test.csv
|   |   |-- y_train.csv
|   |   |-- y_test.csv
|
|-- Models
|   |-- best_model
|   |-- model
|
|-- Notebooks
|   |-- Data_collection.ipynb
|   |-- Data_cleaning.ipynb
|   |-- Preprocessing.ipynb
|   |-- Model_train.ipynb
|   |-- Hyperparameter_tuning.ipynb
|
|-- Src
|   |-- app.py
|   |-- Streamlit.py
|   |-- x.ipynb
```

## Workflow Steps
### 1. Data Collection
- The dataset is stored in the `Raw_Data/Raw.csv` file.
- `Data_collection.ipynb` is used to collect and inspect the dataset.

### 2. Data Cleaning
- The `Data_cleaning.ipynb` notebook is used to handle missing values, outliers, and data inconsistencies.
- The cleaned dataset is saved in `Cleaned_Data/Cleaned_Data.csv`.

### 3. Data Preprocessing
- The `Preprocessing.ipynb` notebook handles feature scaling, encoding, and splitting the dataset.
- The processed data is saved in `preprocess_Data/` as:
  - `X_train.csv`, `X_test.csv`: Features for training and testing
  - `y_train.csv`, `y_test.csv`: Target labels for training and testing

### 4. Model Training
- `Model_train.ipynb` trains multiple models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - AdaBoost Regressor
  - Gradient Boosting Regressor
- The trained models and their performance are evaluated and stored.

#### Model Performance (RMS Error):
```
Linear Regression: 0.3320
Decision Tree Regressor: 0.0403
Random Forest Regressor: 0.0366
AdaBoost Regressor: 0.2730
Gradient Boosting Regressor: 0.1612
```

### 5. Hyperparameter Tuning
- `Hyperparameter_tuning.ipynb` is used to optimize the best-performing model.
- The best model is saved in the `Models/best_model/` directory.

### 6. Model Deployment
- `app.py` loads the best model and provides a user interface for predictions.
- The deployment is handled using Streamlit (`Streamlit.py`).

## How to Run the Project
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <project_directory>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```sh
   streamlit run Src/Streamlit.py
   ```

## Conclusion
This project provides a complete pipeline from data collection to deployment. The best-performing model is selected using hyperparameter tuning and deployed using Streamlit. The structure ensures modularity and reusability for future improvements.


