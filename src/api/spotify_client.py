import os
import requests
from base64 import b64encode


class SpotifyClient:
    def __init__(self):
        # Fetch the Client ID and Client Secret from environment variables
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        
        
        if not self.client_id or not self.client_secret:
            raise ValueError("Please set the environment variables 'SPOTIPY_CLIENT_ID' and 'SPOTIPY_CLIENT_SECRET'")
        
    
    def get_access_token(self):
        # Set your Client ID and Client Secret from Spotify Developer Dashboard
        client_id = self.client_id  # replace with your client_id
        client_secret = self.client_secret  # replace with your client_secret

        # Spotify's Accounts service token URL
        token_url = "https://accounts.spotify.com/api/token"

        # Encode the Client ID and Client Secret in base64 (as required by Spotify)
        client_creds = f"{client_id}:{client_secret}"
        encoded_creds = b64encode(client_creds.encode()).decode()

        # Prepare the headers for the request
        headers = {
            "Authorization": f"Basic {encoded_creds}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Prepare the data to send in the POST request
        data = {
            "grant_type": "client_credentials"
        }

        # Make the POST request to get the access token
        response = requests.post(token_url, headers=headers, data=data)

        # Parse the response as JSON
        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info['access_token']
            print(f"Access Token: {access_token}")
        else:
            print(f"Failed to get access token: {response.status_code}")
            print(response.json())
            access_token = None

        self.access_token = access_token
        return access_token
