import requests, ids

# Set your Postman API key and collection ID
api_key = f"{ids.api_key}"
collection_access_key = f"{ids.collection_access_key}"
collection_id = f"{ids.collection_id}"

# Define the endpoint URLs
get_collection_url = f"https://api.getpostman.com/collections/{collection_id}?access_key={api_key}"



# Set the authentication headers for the API requests
headers = {"X-Api-Key": collection_access_key, "Content-Type": "application/json", "Accept": "application/vnd.postman.v2+json"}

# Send a GET request to get the collection data
response = requests.get(get_collection_url)
collection_data = response.json()["collection"]

# Get the request IDs for all requests in the collection
request_ids = [request["uid"] for request in collection_data["item"]]

# Loop through all request IDs and update the authentication settings
for request_id in request_ids:
    update_request_url = f"https://api.getpostman.com/collections/{collection_id}/requests/{request_id}"

    # Set the request payload to update the authentication settings to "Inherit from parent"
    payload = {"collection" : {"requests": {"properties": {"auth": "" }}}}
    # Send a PUT request to update the request with the new authentication settings
    response = requests.put(
        update_request_url,
        headers=headers,
        json=payload,
    )
    if response.status_code == 200:
        print(f"Updated request {request_id} authentication settings to 'Inherit from parent'" + response.text)
    else:
        # print(f"Failed to update request {request_id} authentication settings" + update_request_url)
        print(update_request_url)
