

// This URL can be changed to the various endpoints we need.
const url = "http://127.0.0.1:5000/education"



d3.json(url,function(error,json){
    if (error) return console.warn(error);
    data = json;
    console.log(data);
})

