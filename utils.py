import requests


def fetch_graphql_data(endpoint, query, variables):
    response = requests.post(endpoint, json={'query': query, 'variables': variables})
    data = response.json()
    if 'errors' in data:
        print(f"Error: {data['errors']}")
        return None
    return data
