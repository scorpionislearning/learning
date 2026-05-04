import requests

try:

    if __name__ == "__main__":
        url = "https://randomuser.me/api/"

        parameters = {
                'results': 50,
                'nat': 'us',
                'gender': 'male'
            }

        response = requests.get(url, params=parameters, timeout=10)
        response.raise_for_status

        if response.status_code == 200:
            data = response.json()

            print(f"Fetched data: {len(data['results'])} users")

            for user in data['results']:
                name = f"{user['name']['first']} {user['name']['last']}"
                print(f"- {name} from {user['nat']}, lives in {user['location']['street']['name']}")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.exceptions.Timeout:
    print("Request timed out. Please try again later.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  

except requests.RequestException as req_err:
    print(f"Error fetching API data: {req_err}")