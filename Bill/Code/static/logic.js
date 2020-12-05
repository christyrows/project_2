

// This URL can be changed to the various endpoints we need.
const url = "http://127.0.0.1:5000/education"



d3.json(url,function(error,json){
    if (error) return console.warn(error);
    data = json;
    console.log(data);
})

// if this d3 function can console log the JSON data from the API,
// then it can also save variables with said data and make plots
// and affix them to map layers on the index.html invocation through
// the flask app.