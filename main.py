from geojson import Point, Feature, FeatureCollection, load
import numpy as np
import csv

def compute_center(outline):
    len = outline.shape[0]
    return np.sum(outline, axis=0)/len

with open('nyc.json') as nyc:
    data = load(nyc)

rows = []
with open('zones_needed.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        rows.append(int(row[0]))
i = 1
writer = csv.writer(open('center_coordinates_needed.csv', 'a+'),delimiter=',')

features = data['features']
for row in rows:
    outline = np.array(features[row-1]['geometry']['coordinates'][0][0])
    center = compute_center(outline)
    writer.writerow([row, center])