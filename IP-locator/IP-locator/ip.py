import geocoder
import folium

g = geocoder.ip('')
g.latlng

my_map1 = folium.Map(location = [],
                    zoom_start= 12)

folium.Marker([],
             popup='Your location' ).add_to(my_map1)

my_map1
