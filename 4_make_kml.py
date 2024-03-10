import pandas as pd
import simplekml

df = pd.read_csv("cleaned.csv")
lats = list(df["Y"])
longs = list(df["X"])
coordinates = []

for i in range(len(lats)):
    coordinates.append((lats[i], longs[i]))

min_lat, min_lon = min(coordinates, key=lambda x: x[0])[0], min(coordinates, key=lambda x: x[1])[1]
max_lat, max_lon = max(coordinates, key=lambda x: x[0])[0], max(coordinates, key=lambda x: x[1])[1]

kml = simplekml.Kml()
polygon = kml.newpolygon(name="Bounding Rectangle",
                         outerboundaryis=[(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat),
                                          (min_lon, max_lat), (min_lon, min_lat)])

kml.save("kml.kml")