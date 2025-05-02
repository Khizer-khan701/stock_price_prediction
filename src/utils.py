import os
import sys
from src.exception import CustomException
from src.logger import logging
import pickle

def get_target(df, target_column):
    # Convert only if dtype is object (string)
    if df[target_column].dtype == 'object':
        cleaned_target = df[target_column].str.replace(r"[$,]", "", regex=True).astype(float)
    else:
        cleaned_target = df[target_column]
    return cleaned_target


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)