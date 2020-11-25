from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# start the flask server
app=Flask(__name__)

# connect to postgresql
# ??????????????????????????????????????????????????????????????????

# First feed the db, then set up function for that data to be fed into the end point of
# the route
# set up a route to the endpoint of the eventual web page and define a function
# that will transfer data from the sql db to the web page

@app.route("/")
def index():
    # DATABASE name is Poverty_and_wellness.  TABLE name will be health_rankings.  table data will be fed
    # from scrape function.
    
   
    return render_template("michal_index.html", data=data)
   

# Route that will trigger the scrape function
@app.route("/scrape_endpt")
def scrape_function():

    # Run the scrape function
   

     # Update the database using updated information
    


    # Redirect the information back to the home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)


