## End to End Machine Learning Project
conda activate venv/
## Src-->Components (It is basically a module)
components can be created as package and that can import in some other location thats why we are creating #__init__.py
## data_ingestion.py
Reading data from specific location that is your data ingestion
## Data_transformer.py
After Ingesting data we need to transform data thus we create data transformer

## Model_trainer.py
training model

## Src-->Pipeline
train_pipeline.py
Fro training pipeline we can call all components

predict_pipeline.py
for prediction of new data

utils.py
functionality which are wring in common way which used in entire application
Like data reading from MomgoDB, Savee model in Cloud


exception.py
Import Sys
Any exception that is getting control then sys libray will have that inforamation


logger.py
whenever you want to do logging you need to import logger

from src.logger import logging
exe: python src/exception.py --> if you want to execute logging in exception file or any another