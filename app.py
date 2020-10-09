from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from config import cxnstring
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

app = Flask(__name__)

engine = create_engine(cxnstring, pool_recycle=3600)
con=engine.connect()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/investors2")
def investors2():
    response = pd.read_sql("SELECT * FROM investors2", con=engine)
    response2_dict = response.to_dict(orient = "records")
    return jsonify(response2_dict)
    
@app.route("/investors_copy")
def investors_copy():
    response2 = pd.read_sql("SELECT * FROM investors_copy", con=engine)
    response3_dict = response2.to_dict(orient = "records")
    return jsonify(response3_dict)

if __name__ == "__main__":
    app.run()
