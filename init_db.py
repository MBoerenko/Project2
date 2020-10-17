import pandas as pd
from sqlalchemy import create_engine
from config import cxnstring

pd.read_csv("final.csv").to_sql(name="final", con = create_engine(cxnstring))