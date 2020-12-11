import numpy as np
import pandas as pd
import datetime as dt 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify, render_template


app=Flask(__name__)

engine = create_engine(f"postgresql://postgres:postgres@localhost/SQLONE")
conn = engine.connect()

base = automap_base()
base.prepare(engine, reflect=True)


session = Session(engine)

@app.route("/")
def index():
    return render_template("index.html", text="Index Page")


@app.route("/crime_data")
def crime_data():
    crime_data_df = pd.read_sql("Select * from crime_stats",conn)
    crime_data_df.rename(columns = {'state_abbr':'State_Abbreviation','state_name': 'State', 'population': 'Population', 'violent_crime': 'Violent_Crime','vio_crime_rate':'Violent_Crime_Rate','violentcrimerank':'Violent_Crime_Rank'}, inplace = True) 
    crime_data_dict=crime_data_df.to_dict(orient='records')
    crime_json = jsonify(crime_data_dict)
    return crime_json

if __name__ == "__main__":
    app.run(debug=True)