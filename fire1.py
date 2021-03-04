import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fire__9_1.json", "w")

fire_data = json.load(infile)
json.dump(fire_data, outfile, indent=4)
# list_of_fire = fire_data["features"]

brights, lons, lats = (
    [],
    [],
    [],
)

for fire in fire_data:
    bright = fire["bright_t31"]
    lon = fire["longitude"]
    lat = fire["latitude"]

    brights.append(bright)
    lons.append(lon)
    lats.append(lat)
if bright > 450:
    print(brights[:10])
"""
k = 450
for i in brights:
    if i > k:
        print(brights[:10])
"""
print(lons[:10])
print(lats[:10])
print(brights[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.03 * bright for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Bright"},
        },
    }
]
my_layout = Layout(title="CA fires Sept 1-13")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="CA_fires.html")
# print(fire_data["features"][0])
# print(fire_data["features"][0]["properties"]["mag"])
