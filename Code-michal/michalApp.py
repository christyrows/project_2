from flask import Flask, render_template, redirect, jsonify
import numpy as np
import pandas as pd
import simplejson as json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.ext.declarative import declarative_base

from config import password
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/Poverty_and_wellness")
conn = engine.connect()
   
session = Session(bind=engine)

# BILL'S CODE TO GET DATA FROM SQL and creating endpoints: reflecting the tables in python classes and querying them
# reflect existing database
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
    rank_data_df.drop("Rank", inplace=True, axis=1) 
    slim_df=rank_data_df.drop([rank_data_df.index[-1], rank_data_df.index[-2]]) 
    slim_df.rename(columns = {"Value":"Variance from Nat'l Average", 'state':'State'}, inplace = True) 
    rank_table=slim_df.to_html(index=False)
    
    return render_template("index.html", table=rank_table)

@app.route("/states")
def states():
    # Create our link from Python to the DB
    session = Session(engine)
   # Query all states
    results = session.query(povState.state).all()
    session.close()
    # Convert list of tuples into normal list
    all_states = list(np.ravel(results))

    return jsonify(all_states)

#/
@app.route("/poverty")
def poverty():
    
    session = Session(engine)
  
    results = session.query(povState.pov_rate).all()
    session.close()
    
    all_pov = list(np.ravel(results))

    return jsonify(all_pov)


@app.route("/education")
def education():
    
    session = Session(engine)
  
    results = session.query(eduState.college_per).all()
    session.close()

    # Convert list of tuples into normal list
    all_edu = list(np.ravel(results))

    return jsonify(all_edu)

# Michal&Christy's code--a different approach to getting the data from sql: Using pandas to read them into dataframes and 
# then creating dictionaries and json objects from the dfs
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
    crime_data_df.rename(columns = {'abbr':'State_Abbreviation','state': 'State', 'pop': 'Population', 
    'vio_crime': 'Violent_Crime','vio_rate':'Violent_Crime_Rate','vio_rank':'Violent_Crime_Rank'}, inplace = True) 
    crime_data_dict=crime_data_df.to_dict(orient='records')
    crime_json = jsonify(crime_data_dict)

    return crime_json

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

    # Do the same thing using reflection method:
    # reflect an existing database into a new model
    #     Base = automap_base()
    # # reflect the tables
    #     Base.prepare(engine, reflect=True)

    #     povState = Base.classes.poverty
    #     eduState = Base.classes.education
    #     vioState=Base.classes.violent_crime
    #     foodState=Base.classes.food_deserts

    #     session = Session(engine)  
    #     results = session.query(foodState.pov_rank,foodState.pov_rate, foodState.state, foodState.desert_rate,foodState.desert_rank,eduState.college_per,eduState.college_rank, vioState.vio_rate,vioState.vio_rank).all()
    #     session.close()
    #     return jsonify(results)


@app.route("/rank_table")
def rank_table():
        
    rank_data_df = pd.read_sql("Select * from state_health_rankings",conn)
    rank_data_df.drop("Rank", inplace=True, axis=1)

    return(rank_data_df.to_html(index=False))

if __name__ == "__main__":
    app.run(debug=True)

  

 