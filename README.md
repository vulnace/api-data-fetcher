API Data Fetcher

A simple Python script to fetch data from an API endpoint and save it to a JSON file.

Features

1- Sends a GET request to a specified API endpoint.

2- Checks for a successful response (HTTP 200).

3- Parses the response into JSON format.

4- Saves the JSON data into a file with a specified name (api-data.json by default).

5- Includes formatted (indented) JSON for better readability.

Requirements Ensure you have Python installed and install the following dependencies using pip:

```
pip install requests
```

Usage

1- Replace "api_endpoint" in the script with your desired API URL.

2- Run the script.

3- If the API responds successfully, the JSON data will be saved in the file api-data.json.


Code Explanation

1- API Request: The script uses the requests library to send a GET request to the provided API URL.

2- Response Handling: Checks the response status code to confirm the request's success (200).

3- Save JSON Data: The JSON response is saved in a file named 'api-data.json' using the json.dump method with indentation for readability.

Example Output

```Success!
{
    "key1": "value1",
    "key2": "value2"
}
Data has been saved to api-data.json
```
