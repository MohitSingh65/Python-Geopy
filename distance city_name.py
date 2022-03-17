from geopy import distance
from geopy import Nominatim
d = distance.distance
g = Nominatim(user_agent="default")
_, wa = g.geocode(input("Enter first city: "))
_, pa = g.geocode(input("Enter second city: "))
print(d(wa, pa).kilometers)
