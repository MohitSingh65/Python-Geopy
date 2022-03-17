from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="GetLoc")
getLoc = loc.geocode(input("Enter Location: "))
print(getLoc.address)
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude =", getLoc.longitude)