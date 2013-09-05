

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

function toPascalCase(str) {
    var arr = str.split(/\s|_/);
    for(var i=0,l=arr.length; i<l; i++) {
        arr[i] = arr[i].substr(0,1).toUpperCase() + 
                 (arr[i].length > 1 ? arr[i].substr(1).toLowerCase() : "");
    }
    return arr.join(" ");
}

  function createMarker(point, map, primary_type, description) {

    var content_window = '<div id="content">'+
      '</div>'+
      '<h2 id="firstHeading" class="firstHeading">' + toPascalCase(primary_type.toLowerCase()) +'</h2>'+
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
            maxWidth: 200,
        });
        infowindow.open(map, marker);
    });
  }

  function initialize(){
      var map_canvas = document.getElementById('map_canvas');
      var map_options = {
        center: new google.maps.LatLng(41.87, -87.62),
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      }
      var map = new google.maps.Map(map_canvas, map_options);
      

      for (var i = 0; i < js_objects.length; i++){
        var point = new google.maps.LatLng(js_objects[i][0], js_objects[i][1]);
        var primary_type = js_objects[i][2];
        var description = js_objects[i][3];

        createMarker(point, map, primary_type, description);

      }
  }

  function initialize2() {
        var mapOptions = {
          zoom: 10,
          center: new google.maps.LatLng(41.87, -87.62),
          mapTypeId: google.maps.MapTypeId.SATELLITE
        };

        map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions);

        var pointArray = new google.maps.MVCArray(crimeData);

        heatmap = new google.maps.visualization.HeatmapLayer({
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