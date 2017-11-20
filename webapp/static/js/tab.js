$( "#tabs" ).tabs();

function myFunc(vars) {
  return vars
}

$("#tablink1").click(function () {
  $.ajax({
    url:'getData/1',
    success: function(response) {
      console.log(response);
      drawGoogleChart(response,1);
    }
  });
})

$("#tablink2").click(function () {
  $.ajax({
    url:'getData/2',
    success: function(response) {
      console.log(response);
      drawGoogleChart(response,2)
    }
  });
})

$("#tablink3").click(function () {
  $.ajax({
    url:'getData/3',
    success: function(response) {
      console.log(response);
      drawGoogleChart(response,3)
    }
  });
})

$("#tablink4").click(function () {
  $.ajax({
    url:'getData/4',
    success: function(response) {
      console.log(response);
      drawGoogleChart(response,4)
    }
  });
})

function drawGoogleChart(response, regId){
  google.charts.load('current', {
    'packages':['geochart'],
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
  });
  google.charts.setOnLoadCallback(drawRegionsMap);

  function drawRegionsMap() {
    var stateobjects = JSON.parse(response);
    var chartdata = google.visualization.arrayToDataTable(stateobjects)

    var options = {
      region: 'US',
      dataMode: 'regions',
      resolution: 'provinces',
      colorAxis: {colors: ['#ead0be', '#d15802']}
    };

    regionId = 'regions_div' + regId
    var chart = new google.visualization.GeoChart(document.getElementById(regionId));

    chart.draw(chartdata, options);
  }
}

function drawBarGraph(){
  google.charts.load('current', {
    packages: ['corechart', 'bar'],
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
  });
  google.charts.setOnLoadCallback(drawAxisTickColors);

  function drawAxisTickColors() {

    $.ajax({
      url:'getChartData',
      success: function(response) {
        console.log(response);
        var stateobjects = $.parseJSON(response);
        var data = google.visualization.arrayToDataTable(stateobjects);

        var options = {
          width: '100%',
          height: '500px',
          title: 'Restaurants vs 18+ Population',
          focusTarget: 'category',
          hAxis: {
            title: 'Restaurant Count',
            format: 'short',
            viewWindow: {
              min: [7, 30, 0],
              max: [17, 30, 0]
            },
            textStyle: {
              fontSize: 14,
              color: '#053061',
              bold: true,
              italic: false
            },
            titleTextStyle: {
              fontSize: 18,
              color: '#053061',
              bold: true,
              italic: false
            }
          },
          vAxis: {
            title: 'Population Count',
            format: 'short',
            textStyle: {
              fontSize: 18,
              color: '#67001f',
              bold: false,
              italic: false
            },
            titleTextStyle: {
              fontSize: 18,
              color: '#67001f',
              bold: true,
              italic: false
            }
          }
        };

        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
        $('#chart_div').css('background-color','white');
      }
    });

  }
}

$('#click2play').click(function(){
  $('#click2play').hide();
  $("#tablink1").click()
})

$('#click2playChart').click(function(){
  $('#click2playChart').hide();
  drawBarGraph();
})