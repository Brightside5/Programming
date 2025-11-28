import requests
import sys

# free Time api https://timeapi.io/swagger/index.html
# timezone info can be found at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# usage: python get_time.py <timezone>

api_url = "https://timeapi.io"

# make the correct api call and extract the current time in that timezone

timezone = sys.argv[1]

# free Time api https://timeapi.io/swagger/index.html
# timezone info can be found at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
url = f"{api_url}/api/time/current/zone?timeZone={timezone}"
response = requests.get(url)
if response.status_code ==  200:
    data = response.json()
    print(f"Time: {data['hour']}: {data['minute']}: {data['seconds']}")
else:
    print("Timezone not found.")
