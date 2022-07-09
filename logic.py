from math import sin, cos, sqrt, atan2, radians

#calculates the distance between two coordinates
#distance unit is in km
def calcDistance(latitude1,longitude1,latitude2,longitude2):
    
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(latitude1)
    lon1 = radians(longitude1)
    lat2 = radians(latitude2)
    lon2 = radians(longitude2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
    #print("Result:", distance)
    #print("Should be:", 278.546, "km")

#load file and converts it into a list of tuples, where each tuple contains a latitude and a longitude
#returns this list
#TODO: find a way to store the file within the repo rather than using my computer lol
def loadFile():

    # empty list to read list from a file
    locations = []

    # open file and read the content in a list
    with open(r'C:/Users/Thaddeus/Downloads/locations.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
        
            x = ''.join(x.split())
            x = tuple(x.split(','))
            temp = []
            for y in x:
                temp.append(float(y))
            # add current item to the list
            locations.append(temp)
    return locations

#finds minimum distance between input coordinate and the list of bins in SG
#returns tuple of the closest bin
def findNearestBin(locations,inputLat,inputLong):
    min = 948309
    minTuple = (0,0)
    for item in locations:
        distance = calcDistance(inputLat, inputLong,item[0],item[1])
        if distance < min:
            min = distance
            minTuple = item
    return minTuple
            
    
# display list
locations = loadFile()
print(len(locations))
print(type(float(locations[0][0])))
print(calcDistance(locations[0][0],locations[0][1],1.391051320483443, 103.9053825116794))
#to find a way to get input from bot
print(findNearestBin(locations[3][0],locations[3][1]))