import requests

try:

    if __name__ == "__main__":
        url = "https://randomuser.me/api/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            user = data['results'][0]
            print(user)

            first_name = user['name']['first']
            last_name = user['name']['last']
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")

            email = user['email']
            country = user['location']['country']
            loc = user['location']['street']['name']
            print(f"Email: {email}")
            print(f"Country: {country}")
            print(f"Location: {loc}")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching API data: {e}")