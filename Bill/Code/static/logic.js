

// This URL can be changed to the various endpoints we need.
const url_edu = "http://127.0.0.1:5000/education"
const url_pov = "http://127.0.0.1:5000/poverty"
const url_states = "http://127.0.0.1:5000/states"



d3.json(url_edu,function(error,json){
    if (error) return console.warn(error);
    data = json;
    console.log(data);
})

d3.json(url_pov,function(error,json){
    if (error) return console.warn(error);
    data = json;
    console.log(data);
})

d3.json(url_states,function(error,json){
    if (error) return console.warn(error);
    data = json;
    console.log(data);
})

// if this d3 function can console log the JSON data from the API,
// then it can also save variables with said data and make plots
// and affix them to map layers on the index.html invocation through
// the flask app.

//save the data as variables

// call plotly with the data, save the plots

// affix the plots to the map/chart/plot layer or the div? using d3, i think?

// Got to find the index template first, though!