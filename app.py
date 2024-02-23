# Import necessary modules
import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv('variables.env')

# API token and endpoint are loaded from environment variables
API_TOKEN = os.getenv('API_TOKEN')
API_ENDPOINT = os.getenv('API_ENDPOINT')

# Define headers for the API request
headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}

def get_tests():
    # Make a GET request to the API endpoint
    response = requests.get(API_ENDPOINT, headers=headers)
    
    # Check if the request was successful (200 is the HTTP status code for "OK")
    if response.status_code == 200:
        # If successful, parse the response as JSON and return it
        return response.json()
    else:
        # If not successful, return an error message
        return {'error': f'Failed to retrieve tests, status code: {response.status_code}'}

if __name__ == '__main__':
    # Get the tests and print them
    tests = get_tests()
    print(tests)