
"""
script : config.py 
purpose: 


"""


# list all required packages needed for specific file imports

import logging
import parsenvy

from pydantic import BaseModel, BaseSettings
from pydantic import (
    BaseModel,
    BaseSettings,
    PostgresDsn,
    HttpUrl,
)






logger = logging.getLogger(__name__)



class Settings(BaseSettings):
    database: PostgresDsn
    mlflow_trackingserver: HttpUrl
    mlflow_experimentname: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"



settings = Settings()

# if you import settings you can access in other files
print(settings.dict())
print(settings.mlflow_experimentname)



try:
    TRACKING_URI = open(".mlflow_uri").read().strip()
except:
    TRACKING_URI = parsenvy.str("MLFLOW_URI")

EXPERIMENT_NAME = "moosic-modeling"







