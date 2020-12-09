from flask import Flask, render_template, redirect, jsonify
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.ext.declarative import declarative_base

from config import password
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/Poverty_and_wellness")
conn = engine.connect()
   
session = Session(bind=engine)

# BILL'S CODE TO GET DATA FROM SQL
povData = pd.read_sql("SELECT * FROM poverty", conn)
eduData = pd.read_sql("SELECT * FROM education", conn)

# reflect an existing database into a new model
Base_bill = automap_base()
# reflect the tables
Base_bill.prepare(engine, reflect=True)

# Save reference to the table
povState = Base_bill.classes.poverty
eduState = Base_bill.classes.education

# start the flask server
app=Flask(__name__)

@app.route("/")
def index():
    
    rank_data_df = pd.read_sql_query("Select * from state_health_rankings",  conn)
    rank_data_df.drop("Value", inplace=True, axis=1)    
    rank_data_df.rename(columns = {'Rank':'Health Rank', 'state':'State'}, inplace = True) 
    rank_table=rank_data_df.to_html(index=False)
    
    return render_template("index.html", table=rank_table)

# BILL'S CODE TO CREATE ENDPOINTS
@app.route("/states")
def states():
    # Create our session (link) from Python to the DB
    session = Session(engine)
   # Query all passengers
    results = session.query(povState.state).all()
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
    results = session.query(povState.pov_rate).all()
    session.close()
    # Convert list of tuples into normal list
    all_pov = list(np.ravel(results))

    return jsonify(all_pov)


@app.route("/education")
def education():
    # Create our session (link) from Python to the DB
    session = Session(engine)
   # Query all passengers
    results = session.query(eduState.college_per).all()
    session.close()

    # Convert list of tuples into normal list
    all_edu = list(np.ravel(results))

    return jsonify(all_edu)


@app.route("/food_deserts",methods=["GET","POST"])
def food_deserts():
    
    food_df = pd.read_sql("Select * from food_deserts", conn) 
    food_dict=food_df.to_dict(orient='records')
    food_json = jsonify(food_dict)
    
    return(food_json)
    
@app.route("/map_data",methods=["GET","POST"])
def map_data():

    map_data_df = pd.read_sql("Select * from health_rankings",conn)
    map_data_df.rename(columns = {'long':'lon'}, inplace = True) 
    map_data_dict=map_data_df.to_dict(orient='records')
    map_json = jsonify(map_data_dict)

    return(map_json)

@app.route("/crime_data")
def crime_data():

    crime_data_df = pd.read_sql("Select * from violent_crime",conn)
    crime_data_df.rename(columns = {'state':'State','vio_rate':'Violent Crime Rate','vio_rank':'Violent Crime Rank'}, inplace = True) 
    crime_data_dict=crime_data_df.to_dict(orient='records')
    crime_json = jsonify(crime_data_dict)
    
    return(crime_json)

@app.route("/combined_data")
def combined_data():
    combined_df=pd.read_sql("Select*from combined_data",conn)
    combined_df.drop(columns=["lat","lon","value"], inplace=True, axis=1)
    combined_df.rename(columns={"collegerank":"College Graduation Rank","collegerate":"College Graduation Rate",
    "fooddesertrank":"Food Desert Rank","healthrank":"Health Rank","povrank":"Poverty Rank","povrate":"Poverty Rate",
    "state":"State","violentcrimerank":"Violent Crime Rank","violentcrimerate":"Violent Crime Rate","popindesert":"Food Desert Rate"},inplace=True)
    combined_dict=combined_df.to_dict(orient='records')
    combined_json=jsonify(combined_dict)

    return combined_json

@app.route("/rank_table")
def rank_table():
    rank_data_df = pd.read_sql("Select * from state_health_rankings",conn)
    rank_data_df.drop("Value", inplace=True, axis=1)
    return(rank_data_df.to_html(index=False))

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

  

 