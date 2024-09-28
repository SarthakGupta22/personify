import os
import requests
from base64 import b64encode
<<<<<<< HEAD
import typing
=======
>>>>>>> main


class SpotifyClient:
    def __init__(self):
        # Fetch the Client ID and Client Secret from environment variables
<<<<<<< HEAD
        self.client_id: str = os.getenv("SPOTIFY_CLIENT_ID", "")
        self.client_secret: str = os.getenv("SPOTIFY_CLIENT_SECRET", "")

        # Ensure that Client ID and Client Secret are set, raise an error if not
        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Please set the environment variables 'SPOTIPY_CLIENT_ID' and 'SPOTIPY_CLIENT_SECRET'"
            )

        # Access token will be stored after it's fetched
        self.access_token: typing.Optional[str] = None

    def get_access_token(self) -> typing.Optional[str]:
        """
        Fetches an OAuth access token from Spotify's API using Client Credentials Flow.
        Returns the access token if successful, otherwise returns None.
        """

        # Client ID and Client Secret are taken from class attributes
        client_id: str = self.client_id
        client_secret: str = self.client_secret

        # Spotify's Accounts service token URL
        token_url: str = "https://accounts.spotify.com/api/token"

        # Encode the Client ID and Client Secret in base64 (as required by Spotify)
        client_creds: str = f"{client_id}:{client_secret}"
        encoded_creds: str = b64encode(client_creds.encode()).decode()

        # Prepare the headers for the request, including the encoded credentials
        headers: typing.Dict[str, str] = {
            "Authorization": f"Basic {encoded_creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # Prepare the data to send in the POST request, specifically the grant type
        data: typing.Dict[str, str] = {"grant_type": "client_credentials"}

        # Make the POST request to get the access token
        response: requests.Response = requests.post(token_url, headers=headers, data=data)

        # Parse the response and check if the request was successful
        if response.status_code == 200:
            token_info: typing.Dict[str, typing.Any] = response.json()
            access_token: str = token_info.get("access_token", "")
            print(f"Access Token: {access_token}")
        else:
            # Log error in case the request fails
=======
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
>>>>>>> main
            print(f"Failed to get access token: {response.status_code}")
            print(response.json())
            access_token = None

<<<<<<< HEAD
        # Store access token in the class and return it
        self.access_token = access_token
        return access_token

    def get_song_features(self, track_id: str) -> typing.Dict[str, typing.Any]:
        """
        Fetches the audio features of a given Spotify track using its track ID.
        Returns a dictionary containing the track's audio features.
        """
        
        # Fetch the access token (if it's not available, make the request to get it)
        access_token: typing.Optional[str] = self.get_access_token()

        # Ensure that an access token was successfully retrieved
        if not access_token:
            raise ValueError("Access token could not be retrieved.")

        # Define the endpoint for getting audio features for the specific track
        url: str = f"https://api.spotify.com/v1/audio-features/{track_id}"

        # Set up headers with the authorization token
        headers: typing.Dict[str, str] = {"Authorization": f"Bearer {access_token}"}

        # Send GET request to the Spotify API
        response: requests.Response = requests.get(url, headers=headers)

        # Parse and return the JSON response containing the audio features
        audio_features: typing.Dict[str, typing.Any] = response.json()

        return audio_features


# Example Usage
spotify_client = SpotifyClient()
song_track_id = "4uLU6hMCjMI75M1A2tKUQC"
print(spotify_client.get_song_features(song_track_id))
=======
        self.access_token = access_token
        return access_token
>>>>>>> main
