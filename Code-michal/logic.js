

// Create food_desert chart
var svgWidth = 1000;
var svgHeight = 650;

var margin = {
    top: 50,
    right: 0,
    bottom: 70,
    left: 20
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select("#foodChart")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Import data and create function to build chart
d3.json("/food_deserts").then(function(foodData) {

    // Scale the data to size of chart
    var xLinearScale = d3.scaleLinear()
        .domain([9, d3.max(foodData, d => d.desert_rate) + 2])
        .range([0, width]);

    var yLinearScale = d3.scaleLinear()
        .domain([d3.min(foodData, d => d.pov_rate) - 1, d3.max(foodData, d => d.pov_rate)])
        .range([height, 0]);

    //Add axes to the chart
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    chartGroup.append("g")
        .call(leftAxis);

    // Create axes labels
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 30 - margin.left)
        .attr("x", 0 - (height / 1.8))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Poverty Rate");

    chartGroup.append("text")
        .attr("transform", `translate(${width / 2.6}, ${height + margin.top })`)
        .attr("class", "axisText")
        .text("Percent Population Living in Food Deserts");


    // Draw the markers and plot them by their x and y coordinates
    circlesGroup = chartGroup.selectAll("circle")
        .data(foodData)
        .enter()
        .append("circle")
        .attr("class", "stateCircle")
        .attr("cx", d => xLinearScale(d.desert_rate))
        .attr("cy", d => yLinearScale(d.pov_rate))
        .attr("r", "22")
        .attr("color", "rgb(89, 89, 201)")
        .attr("opacity", ".5")

    // Insert abbreviated state names into markers
    chartGroup.append("g").selectAll("text")
        .data(foodData)
        .enter()
        .append("text")
        .attr("class", "stateText")
        .attr("x", d => xLinearScale(d.desert_rate))
        .attr("y", d => yLinearScale(d.pov_rate))
        .text(function(d) {
            return d.abbr;
        })

    // Add tooltips with poverty and food desert data
    var toolTip = d3.tip()
        .attr("class", "d3-tip")
        .offset([80, -60])
        .html(function(d) {
            return (`${d.state}<br>Poverty Rate: ${d.pov_rate}<br>Food Desert Rate: ${d.desert_rate},<br>Poverty Rank: ${d.pov_rank}<br>Food Desert Rank: ${d.desert_rank}`);
        });

    // // Set up event handler to trigger the tooltip on hover

    circlesGroup.call(toolTip);

    circlesGroup.on("mouseover", function(data) {
            toolTip.show(data, this);
        })
        .on("mouseout", function(data, index) {
            toolTip.hide(data);

        })

}).catch(function(error) {
    console.log(error);
})

// Creating map object
var myMap = L.map("map", {
    center: [46, -115],
    zoom: 4
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/outdoors-v11",
    accessToken: mapbox_token
}).addTo(myMap);

d3.json("/map_data").then(function(d) {
    stateArray = []
    stateRank = []
    for (var i = 0; i < d.length; i++) {
        var lon = d[i].lon
        var lat = d[i].lat
        var state = d[i].state
        var rank = d[i].rank
        var pov_rank = d[i].pov_rank
        var food_rank = d[i].food_rank
        var college_rank = d[i].college_rank
        var vio_rank = d[i].vio_rank
        stateArray.push(state)
        stateRank.push(rank)
        L.marker([lat, lon]).bindPopup(`<h5>${state}</h5>Rankings</5> <hr>Health: ${rank}<br>Poverty: ${pov_rank}`).addTo(myMap);
    }
    // L.choropleth(d), {
    //     valueProperty: stateRank,
    //     scale: ["#fad635", "#c9d841", "#13ae52", "#02B9ed", "#2979b9"],
    //     steps: 5,
    //     mode: "q",
    //     style: {
    //         // Border color
    //         color: "#fff",
    //         weight: 1,
    //         fillOpacity: 0.8
    //     }
    // }
})

// Set up the legend
var legend = L.control({ position: "topright" });
legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var limits = [1, 10, 20, 30, 40, 50];
    var colors = ["#ff4500", "#FFA500", "#FFD700", "#ADFF2F", "#008000"]
    var labels = [];
    // console.log(colors)
    // Add min & max
    var legendInfo = "<h5>States' Health Rankings</h5>" +
        "<div class=\"labels\">" +
        "<div class=\"min\">" + limits[limits.length - 1] + "</div>" +
        "<div class=\"max\">" + limits[0] + "</div>" +
        "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
        labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul style='text-align:center'>" + labels.join("") + "</ul>";
    return div;
};

legend.addTo(myMap);


d3.json("/combined_data").then(function(d) {

    var stateArray = []
    for (var i = 0; i < d.length; i++) {
        var state = d[i].State
        stateArray.push(state)
    }
    // console.log(stateArray)

    d3.select("#selectState").selectAll("option")
        .data(stateArray)
        .enter()
        .append("option")
        .html(function(d) {
            return `<option>${d}</option>`
        });

    d3.selectAll("#selectState").on("change", handleSubmit)

    function handleSubmit() {

        d3.event.preventDefault();

        populatePanel();
    }

    function populatePanel() {

        var stateInput = d3.select("#selectState").node().value;
        // console.log(stateInput)

        var dataIndex = stateArray.indexOf(stateInput)
        console.log(dataIndex)

        var dropDown = d[dataIndex]

        var selection = d3.select(".panel-body").html("")
        Object.entries(dropDown).forEach(([key, value]) => {
            selection.append("p").text(`${key}: ${value}`)
        })
    }
})