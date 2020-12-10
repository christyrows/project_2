const url_pov = "/poverty"
const url_crime = "/crime_data"

var crime_data = [];
var pov_data = [];

d3.json(url_crime).then(function(crime_data){
  d3.json(url_pov).then(function(pov_data){

    console.log(crime_data);

    var trace1 = {
        x: crime_data.map(row => row.State),
        y: crime_data.map(row => row.Violent_Crime),
        name: 'State Crime',
        type: 'line',
      };

      var trace2 = {
        x: crime_data.map(row => row.State),
        y: pov_data,
        name: 'State Poverty',
        type: 'line',
      };

    var data = [trace1, trace2];
          
    var layout = {
        title: "State vs. Crime Rate",
        xaxis: { title: "State" },
        yaxis: { title: "Violent Crime Rate" }
      };
      

      Plotly.newPlot("bar-plot", data, layout);
        
  })
})
