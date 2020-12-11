import numpy as np
import pandas as pd 
import datetime as dt
import simplejson as json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, render_template, redirect

# start the flask server
app=Flask(__name__)


#################################################
# Database Setup
#################################################
engine_bill = create_engine("postgresql://postgres:postgres@localhost/state_poverty")
conn_bill = engine_bill.connect()

povData = pd.read_sql("SELECT * FROM poverty_by_state", conn_bill)
eduData = pd.read_sql("SELECT * FROM education_by_state", conn_bill)

# reflect an existing database into a new model
Base_bill = automap_base()
# reflect the tables
Base_bill.prepare(engine_bill, reflect=True)

# Save reference to the table
povState = Base_bill.classes.poverty_by_state
eduState = Base_bill.classes.education_by_state


@app.route("/")
def index():
    
    return render_template('index.html')
   

@app.route("/states")
def states():
    # Create our session (link) from Python to the DB
    session = Session(engine_bill)
   # Query all passengers
    results = session.query(povState.state_name).all()
    session.close()
    # Convert list of tuples into normal list
    all_states = list(np.ravel(results))

    return jsonify(all_states)

#/
@app.route("/poverty")
def poverty():
    # Create our session (link) from Python to the DB
    session = Session(engine_bill)
   # Query all passengers
    results = session.query(povState.poverty_pct).all()
    session.close()
    # Convert list of tuples into normal list
    all_pov = list(np.ravel(results))

    return jsonify(all_pov)


@app.route("/education")
def education():
    # Create our session (link) from Python to the DB
    session = Session(engine_bill)
   # Query all passengers
    results = session.query(eduState.education_pct).all()
    session.close()

    # Convert list of tuples into normal list
    all_edu = list(np.ravel(results))

    return jsonify(all_edu)


if __name__ == "__main__":
    app.run(debug=True)


