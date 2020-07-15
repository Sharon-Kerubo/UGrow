            function CreateMap(lat,long){
            var mymap = L.map('mapid').setView([lat, long], 13);
                L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWlzc2dlZWsiLCJhIjoiY2s1cWlyODc4MDJyZTNlbWxnbHp4dnVjYSJ9.b5iJpCc0ypglLOvc5DDj1A', {
                         attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 12,
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1,
            }).addTo(mymap);
            }
            function popUp(f,l){
                var out = [];
                if (f.properties){
                    for(key in f.properties){
                        out.push(key+": "+f.properties[key]);
                    }
                    l.bindPopup(out.join("<br />"));
                }
            }

            function initialize() {
                navigator.geolocation.getCurrentPosition(
                  function(p) {
                    // console.log(p.coords.latitude,p.coords.longitude);
                    CreateMap(p.coords.latitude, p.coords.longitude);
                  },
                  function(err) {
                    switch (error.code) {
                          case error.PERMISSION_DENIED:
                              alert('User denied the request for Geolocation.');
                              break;
                          case error.POSITION_UNAVAILABLE:
                              alert('Position information is unavailable.');
                              break;
                          case error.TIMEOUT:
                              alert('The request to get user position timed out.');
                              break;
                          case error.UNKNOWN_ERROR:
                              alert('An unknown error occurred.');
                              break;
                      }
                  }
                );
            }
            window.onload = initialize;