//Marker Map initialize function
function initialize()
{
    var map_canvas = document.getElementById('map_canvas');
    var map_options = 
    {
      center: new google.maps.LatLng(41.87, -87.62),
      zoom: 12,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    var map = new google.maps.Map(map_canvas, map_options);
    
    loopObj(map, js_objects);
}

//set up the autocomplete in the search bar
$(function(){
    var tags = new Array();

    for (var i=0; i<neighborhoodNames.length; i++){
      tags.push(toPascalCase(neighborhoodNames[i]));
    };

    $("#search").autocomplete({
      source: tags
    });
  });


//Allows keyboard key 'enter' to be pressed for submission
$(document).ready(function(){
  $('#search').keypress(function(event){
    if(event.which == 13){
      event.preventDefault();
      mapNeigh();
    }
  });
});


//Allows submit click
$(document).ready(function(){
  $('#submit').click(function(){
    mapNeigh();
  });
});

//Clears the search bar when clicked
$(document).ready(function(){
  $('input:text').click(
      function(){
          $(this).val('');
      });
});

//retrive the neighborhood polygon based on the input in the search bar
function mapNeigh(){
  
  var searchterm = (document.getElementById("search").value).toLowerCase();
  var areaNum = neighborhood_obj[searchterm][0];
  var areaCrimeList = new Array();

  for(var i=0; i<js_objects.length; i++){
    if(js_objects[i][4] == areaNum){
      areaCrimeList.push(js_objects[i])
    }    
  };

  google.maps.event.addDomListener(window, 'load', createNeighborhood(neighborhood_obj[searchterm], areaCrimeList));
  
}


function submitCrimes(field){
  var map_canvas = document.getElementById('map_canvas');
  var map_options = {
    center: new google.maps.LatLng(41.87, -87.62),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(map_canvas, map_options);

  var checkCount = 0;

  for (var i = 0; i < field.length; i++){
    if (field[i].checked){
      checkCount ++;
      var crime_type = (field[i].value);
      for(var j in js_objects){
        if(js_objects[j][2] == crime_type){
          var point = new google.maps.LatLng(js_objects[j][0], js_objects[j][1]);
          var primary_type = js_objects[j][2];
          var description = js_objects[j][3];

          createMarker(point, map, primary_type, description);
        }
      }
    }   
  }

  if (checkCount == 0){
    initialize();
  }
    
}

//Return a string which first letter of word is uppercase
function toPascalCase(str) {
    var arr = str.split(/\s|_/);
    for(var i=0,l=arr.length; i<l; i++) {
        arr[i] = arr[i].substr(0,1).toUpperCase() + 
                 (arr[i].length > 1 ? arr[i].substr(1).toLowerCase() : "");
    }
    return arr.join(" ");
}

//Create a marker with an infowindow
function createMarker(point, map, primary_type, description) {

  var content_window = '<div id="window-content">'+
    '</div>'+
    '<h2 id="firstHeading">' + toPascalCase(primary_type.toLowerCase()) +'</h2>'+
    '<div id="bodyContent">'+
    '<p>'+ description.toLowerCase() + '</p>' +
    '</div>';

  var marker = new google.maps.Marker({
        position: point,
        map: map,
  });

  google.maps.event.addListener(marker, 'click', function() {
      if (infowindow) {
         infowindow.close();
      };
      infowindow = new google.maps.InfoWindow({
          content: content_window,
        
      });
      infowindow.open(map, marker);
  });
  //marker.setMap(map);
}


function createNeighborhood(neighborhood, crimeList){

  var neighCoords = neighborhood[1];
  var neighNum = neighborhood[0];
  var map_canvas = document.getElementById('map_canvas');
  var farCoord = Math.round((neighCoords.length)/2);
  var x1 = neighCoords[0][0];
  var y1 = neighCoords[0][1];
  var x2 = neighCoords[farCoord][0];
  var y2 = neighCoords[farCoord][1];
  var midPointX = (x1+x2)/2;
  var midPointY = (y1+y2)/2;

  var map_options = 
  {
    center: new google.maps.LatLng(midPointX, midPointY),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(map_canvas, map_options);
  var boundariesPolygon;
  var Coords = new Array();

  for(var i=0; i<neighCoords.length; i++){
    Coords[i] = new google.maps.LatLng(neighCoords[i][0], neighCoords[i][1]);
  }

  boundariesPolygon = new google.maps.Polygon({
    paths: Coords,
    strokeColor: '#FF0000',
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: '#FF0000',
    fillOpacity: 0.35
  });

  boundariesPolygon.setMap(map);
  loopObj(map, crimeList);

}

//loop through js_obj to create a list ready to make markers
function loopObj(map, list){
 for (var i = 0; i < list.length; i++)
  { 
    var lat = list[i][0];
    var longi = list[i][1];
    var point = new google.maps.LatLng(lat,longi);
    var primary_type = list[i][2];
    var description = list[i][3];

    createMarker(point, map, primary_type, description);
  }
}



//Heat map itinialize function
function initialize2() 
{
  var mapOptions = 
  {
    zoom: 10,
    center: new google.maps.LatLng(41.87, -87.62),
    disableDoubleClickZoom: true,
    mapTypeId: google.maps.MapTypeId.SATELLITE
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var pointArray = new google.maps.MVCArray(crimeData);

  heatmap = new google.maps.visualization.HeatmapLayer(
  {
    data: pointArray
  });

  heatmap.setMap(map);
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.setOptions({
    gradient: heatmap.get('gradient') ? null : gradient
  });
}

function changeRadius() {
  heatmap.setOptions({radius: heatmap.get('radius') ? null : 20});
}

function changeOpacity() {
  heatmap.setOptions({opacity: heatmap.get('opacity') ? null : 0.2});
}