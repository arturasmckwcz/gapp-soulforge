import requests

from setup import setup


def get_graphql_data(query):
    url = setup.api_url
    headers = {"Content-Type": "application/json"}
    data = {"query": query}

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if "data" in response_json:
        return response_json["data"]
    else:
        # Handle error cases
        error_message = response_json["errors"][0]["message"]
        raise Exception(f"GraphQL request failed: {error_message}")
