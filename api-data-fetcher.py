import requests
import json

#Provide an API endpoint.
url = "api_endpoint"
req = requests.get(url)

if req.status_code == 200:
    print("Success!")
    data = req.json()
    print(json.dumps(req.json(), indent=4))

    #Assign a name to the file, in this case, it's api-data.json.
    file_name = 'api-data.json'
    
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Data has been saved to {file_name}")
else:
    print(f"Failed to retrieve data. Status code: {req.status_code}")
