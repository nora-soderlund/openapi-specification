# [START maps_http_directions_boston_concord_waypoints_now]
import requests

url = "https://maps.googleapis.com/maps/api/directions/json?origin=Boston, MA&destination=Concord, MA&waypoints=via:Charlestown,MA|via:Lexington,MA&departure_time=now&key=YOUR_API_KEY"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# [END maps_http_directions_boston_concord_waypoints_now]