// This URL can be changed to the various endpoints we need.
const url_edu = "http://127.0.0.1:5000/education"
const url_pov = "http://127.0.0.1:5000/poverty"
const url_states = "http://127.0.0.1:5000/states"

var edu_data = [];
var pov_data = [];
var states_data = [];


// ------------------------------- start of D3.json statements
// Education JSON
d3.json(url_edu, function(error, json) {
    if (error) return console.warn(error);
    data = json;
    edu_data = data;

    // Poverty JSON
    d3.json(url_pov, function(error, json) {
        if (error) return console.warn(error);
        data = json;
        pov_data = data;

        //States JSON
        d3.json(url_states, function(error, json) {
            if (error) return console.warn(error);
            data = json;
            states_data = data;



            console.log("Education");
            console.log(edu_data);

            console.log("Poverty");
            console.log(pov_data);

            console.log("States");
            console.log(states_data);

            console.log("-------------------");


            //D3 double bar graph code goes in here!

            var trace1 = {
                x: states_data,
                y: edu_data,
                name: 'Education Pct',
                type: 'bar'
            };

            var trace2 = {
                x: states_data,
                y: pov_data,
                name: 'Poverty Pct',
                type: 'bar'
            };

            var data = [trace1, trace2];

            var layout = { barmode: 'group' };

            Plotly.newPlot('educationChart', data, layout);

            /*

    

            */




        })

    })

})



// save the plots as fig.png files
// Have this done by EOD tuesday

//--------------------------------------------

// affix the plots to the map/chart/plot layer or the div? using d3, i think?

// Got to find the index template first, though!