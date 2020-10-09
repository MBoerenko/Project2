import pandas as pd
from sqlalchemy import create_engine
from config import cxnstring

pd.read_csv("investors_copy.csv").to_sql(name="investors_copy", con=create_engine(cxnstring))
pd.read_csv("investors2.csv").to_sql(name="investors2", con=create_engine(cxnstring))