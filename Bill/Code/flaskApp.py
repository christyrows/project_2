import numpy as np
import pandas as pd 
import datetime as dt

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

eduData = pd.read_sql("SELECT * FROM education_by_state", conn)

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

# Save reference to the table
#State = Base.classes.state_name


@app.route("/")
def index():
    
   
    return render_template('index.html')
   

@app.route("/states")
def states():

    # Create our session (link) from Python to the DB
    session = Session(engine)

   # Query all passengers
    results = session.query(State.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_states = list(np.ravel(results))

    return jsonify(all_states)

    


    # Redirect the information back to the home page
    #return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)


