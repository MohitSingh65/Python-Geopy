from geopy import distance
location1 = input("Enter the coordinates for first location: ")
location2 = input("Enter the coordinates for second location: ")
print(distance.distance(location1, location2).kilometers)