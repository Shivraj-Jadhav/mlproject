import os
import sys
from src.exception import CustomException

import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)


        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e,sys)
    

import pickle  # Or dill if needed

def load_object(file_path):
    """Loads an object from a file.

    Args:
        file_path: The path to the file containing the object.

    Returns:
        The loaded object.

    Raises:
        FileNotFoundError: If the file does not exist.
        pickle.UnpicklingError: If there's an error unpickling the object.
    """

    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except FileNotFoundError as e:
        print(f"Error: File not found: {file_path}")
        raise e
    except pickle.UnpicklingError as e:
        print(f"Error unpickling object from {file_path}")
        raise e
