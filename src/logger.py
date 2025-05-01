import os
import sys
import logging
import datetime
from src.exception import CustomException

LOG_FILE=f"{datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
file_path=os.path.join(os.getcwd(),"Logs")
os.makedirs(file_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(file_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO
)


if __name__=="__main__":
    try:
        logging.info("error occured")
    except Exception as e:
        raise CustomException(e,sys)