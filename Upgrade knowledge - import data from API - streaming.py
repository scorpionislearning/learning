import requests

def connect():
    try:

        response = requests.get(
            'https://stream.wikimedia.org/v2/stream/page-create',
            stream=True,
            headers={'Accept': 'text/event-stream','User-Agent': 'MyTestApp/1.0 (haryadi.santoso@gmail.com)'}
        )
        print(f"Response status code: {response.status_code}")

        for line in response.iter_lines():
            if line:
                decoded = line.decode('utf-8')
                if decoded.startswith('data: '):
                    data = decoded[6:]
                    try:
                        import json
                        print(json.dumps(json.loads(data), indent=2))
                    except:
                        print(data)

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  

    except requests.RequestException as req_err:
        print(f"Error fetching API data: {req_err}")
    
    finally:
        print("Finished streaming data.")

if __name__ == "__main__":
    connect()