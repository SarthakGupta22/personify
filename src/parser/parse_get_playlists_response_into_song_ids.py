import json

# Sample Request from https://developer.spotify.com/documentation/web-api/reference/get-playlist
"""
curl --request GET \
  --url 'https://api.spotify.com/v1/playlists/4XT99DDYGtPtQLZybi0Gwt?fields=tracks%28items%28track%28id%29%29%29' \
  --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
"""

def get_track_ids(file_path):
    """
    Reads a JSON file and extracts the track IDs.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    list: A list of track IDs.
    """
    try:
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            # Parse the JSON data
            parsed_data = json.load(file)
        
        # Extract track IDs into a list
        track_ids = [item['track']['id'] for item in parsed_data['tracks']['items']]
        
        return track_ids
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing file: {e}")
        return []

# Example usage
file_path = 'sample_data/get_playlist_response.json'
track_ids = get_track_ids(file_path)
print(track_ids)

### Sample response
['2oENJa1T33GJ0w8dC167G4', '2gpWyfu7eZ01zzncHpxOtA', '0k1WUmIRnG3xU6fvvDVfRG']
