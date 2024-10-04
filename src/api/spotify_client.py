import os
import requests
import sys
from base64 import b64encode
from typing import Any
from datetime import datetime, timedelta
from src.api.response_types import AudioFeatures
from src.parser.parse_get_playlists_response_into_song_ids import parse_playlists_response_into_data

class SpotifyClient:
    def __init__(self):
        # Fetch the Client ID and Client Secret from environment variables
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID", "")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")

        # Ensure that Client ID and Client Secret are set, raise an error if not
        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Please set the environment variables 'SPOTIFY_CLIENT_ID' and 'SPOTIFY_CLIENT_SECRET'"
            )

        # Access token will be stored after it's fetched
        self.access_token = None
        self.token_created_at = None

    def get_access_token(self) -> str | None:
        """
        Fetches an OAuth access token from Spotify's API using Client Credentials Flow.
        Returns the access token if successful, otherwise returns None.
        """

        # If the access token exists and is still valid (within 1 hour), return it
        
        if self.access_token and self.token_created_at:
            time_since_creation = datetime.now() - self.token_created_at
            if time_since_creation < timedelta(hours=1):
                # Access token is still valid
                print("Access token is still valid.")
                return self.access_token

        # Client ID and Client Secret are taken from class attributes
        client_id = self.client_id
        client_secret = self.client_secret

        # Spotify's Accounts service token URL
        token_url = "https://accounts.spotify.com/api/token"

        # Encode the Client ID and Client Secret in base64 (as required by Spotify)
        client_creds = f"{client_id}:{client_secret}"
        encoded_creds = b64encode(client_creds.encode()).decode()

        # Prepare the headers for the request, including the encoded credentials
        headers = {
            "Authorization": f"Basic {encoded_creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # Prepare the data to send in the POST request, specifically the grant type
        data = {"grant_type": "client_credentials"}

        # Make the POST request to get the access token
        response = requests.post(token_url, headers=headers, data=data)

        # Parse the response and check if the request was successful
        if response.status_code == 200:
            token_info = response.json()
            access_token = token_info.get("access_token", "")
        else:
            # Log error in case the request fails
            print(f"Failed to get access token: {response.status_code}")
            print(response.json())
            access_token = None

        # Store access token in the class and return it
        self.access_token = access_token
        self.token_created_at = datetime.now()
        return access_token

    def get_song_ids(self, query: str) -> dict[str, Any]:
        """
        Fetches the Spotify track IDs for a given query using the Spotify Search API.
        Returns a dictionary containing the track IDs.
        """

        # Fetch the access token (if it's not available, make the request to get it)
        access_token = self.get_access_token()

        # Ensure that an access token was successfully retrieved
        if not access_token:
            raise ValueError("Access token could not be retrieved.")

        # Define the endpoint for searching tracks on Spotify
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}?fields=tracks%28items%28track%28id%29%29%29"

        # Set up headers with the authorization token
        headers = {"Authorization": f"Bearer {access_token}"}

        # Send GET request to the Spotify API
        response = requests.get(url, headers=headers)

        # Parse and return the JSON response containing the track IDs
        track_ids = response.json()
        return track_ids

    def get_song_features(self, track_id: str) -> dict[str, Any]:
        """
        Fetches the audio features of a given Spotify track using its track ID.
        Returns a dictionary containing the track's audio features.
        """
        
        # Fetch the access token (if it's not available, make the request to get it)
        access_token = self.get_access_token()

        # Ensure that an access token was successfully retrieved
        if not access_token:
            raise ValueError("Access token could not be retrieved.")

        # Define the endpoint for getting audio features for the specific track
        url = f"https://api.spotify.com/v1/audio-features/{track_id}"

        # Set up headers with the authorization token
        headers = {"Authorization": f"Bearer {access_token}"}

        # Send GET request to the Spotify API
        response= requests.get(url, headers=headers)

        # Parse and return the JSON response containing the audio features
        audio_features = response.json()

        return audio_features

    
    def get_all_song_features(self, track_ids: list[str]) -> list[dict[str, Any]]:
        pass

# Run function
# python3 src/api/spotify_client.py 3cEYpjA9oz9GiPac4AsH4n
if __name__ == "__main__":
    # Check if a playlist ID is passed via command line
    if len(sys.argv) > 1:
        playlist_id = sys.argv[1]
    else:
        # Default playlist ID if none is passed
        playlist_id = "3cEYpjA9oz9GiPac4AsH4n"

    spotify_client = SpotifyClient()

    song_ids_response = spotify_client.get_song_ids(playlist_id)
    print("Spotify GetPlaylist Response:", song_ids_response)

    # parser
    song_ids_list = parse_playlists_response_into_data(song_ids_response)
    print("Parsed Song IDs:", song_ids_list)

    # # Get the audio features for a specific song
    # pprint(spotify_client.get_song_features(song_track_id))
    # pprint(AudioFeatures(**spotify_client.get_song_features(song_track_id)).model_dump())
