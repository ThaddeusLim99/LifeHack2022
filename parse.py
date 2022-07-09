import os
from pykml import parser
import sys

# Root directory of the project
ROOT_DIR = os.getcwd()
kml_file = os.path.join(ROOT_DIR, "RECYCLINGBINS.kml")

with open(kml_file) as f:
    doc = parser.parse(f).getroot()

f = open("locations.txt", "w")

# Get coordinates in the google map format
for p in doc.Document.Folder.Placemark:
    deg1, deg2, _ = p.Point.coordinates.text.split(',')
    f.write(f'{deg2}, {deg1}\n')

f.close()

# Get building name of the placemark
# for p in doc.Document.Folder.Placemark:
#         d = p.description.text.splitlines()
#         d = list(filter(None, d))
#         isName = False
#         for line in d:
#             if isName:
#                 name = line
#                 isName = False
#             if line == "<td>ADDRESSBUILDINGNAME</td>":
#                 isName = True
#         _,name = name.split("<td>")
#         name,_ = name.split("</td>")
#         print(name)