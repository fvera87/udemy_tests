import folium
import pandas

volcanoes = pandas.read_csv("volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
name = list(volcanoes["NAME"])
elev = list(volcanoes["ELEV"])

# world_json = pandas.read_json("world.json")
# print(world_json)


def get_color(elevation):
    if elevation > 2000.0:
        return "red"
    elif elevation > 1000:
        return "orange"
    else:
        return "green"


map = folium.Map([48.7767982,-121.8109970], zoom_start=3)
fg = folium.FeatureGroup("Markers")
for lat,lon, n, el in zip(lat, lon, name, elev):
    fg.add_child(folium.CircleMarker(location=[lat,lon], radius=8, popup=folium.Popup(n, parse_html=True), color="grey",
                                     fill_opacity=0.7, fill_color=get_color(el), fill=True))

fg2 = folium.FeatureGroup("CountryPopulation")
fg2.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fg2)

map.add_child(folium.LayerControl())
map.save("Map.html")