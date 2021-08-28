import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def approve_destination_fingerprint():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/fingerprints'

    # Adjust the payload settings to
    # reflect your settings from the
    # documentation.
    #
    # You need to insert your values next
    # to the appropiate key.
    payload = {
        'destination_id': 'YOUR_CONNECTOR',
        'hash': 'YOUR_HASH',
        'public_key': 'YOUR_PUBLIC_KEY'
    }

    response = requests.post(url=endpoint, auth=base64, json=payload).json()
    print(response)