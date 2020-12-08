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
engine = create_engine("postgresql://postgres:postgres@localhost/state_poverty")
conn = engine.connect()

povData = pd.read_sql("SELECT * FROM poverty_by_state", conn)
eduData = pd.read_sql("SELECT * FROM education_by_state", conn)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
povState = Base.classes.poverty_by_state
eduState = Base.classes.education_by_state

#print("..")
#print("..")
#print("..")
#print("NOW PRINTING EDUDATA")
#print("..")
#print(f"{eduData}")
#print("..")
#print("NOW PRINTING BASE:")
#print("..")
#print(f"{Base.classes.poverty_by_state.state_name}")


@app.route("/")
def index():
    
    return render_template('index.html')
   

@app.route("/states")
def states():
    # Create our session (link) from Python to the DB
    session = Session(engine)
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
    session = Session(engine)
   # Query all passengers
    results = session.query(povState.poverty_pct).all()
    session.close()
    # Convert list of tuples into normal list
    all_pov = list(np.ravel(results))

    return jsonify(all_pov)

    
################################################################
##
##  Ultimately this API route will have the graph or graphs of the 
##  poverty v education data, as well as the standardized navbar and
##  format detail in proper order.
##
##  It will then return a render template of the education.html
##  file which will be stored in the templates file.
##
##  This pattern must be followed for the other teammates' data.
##
##  :  individual.html, in templates folder, 
##     api route renders template of file
##
################################################################

@app.route("/education")
def education():
    # Create our session (link) from Python to the DB
    session = Session(engine)
   # Query all passengers
    results = session.query(eduState.education_pct).all()
    session.close()

    # Convert list of tuples into normal list
    all_edu = list(np.ravel(results))

    return jsonify(all_edu)


if __name__ == "__main__":
    app.run(debug=True)


