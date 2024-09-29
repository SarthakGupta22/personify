import pytest
from src.api.response_types import AudioFeatures

def test_valid_audio_features():
    valid_data = {
        "acousticness": 0.5,
        "analysis_url": "https://api.spotify.com/v1/audio-analysis/track_id",
        "danceability": 0.8,
        "duration_ms": 210000,
        "energy": 0.7,
        "id": "track_id",
        "instrumentalness": 0.0,
        "key": 5,
        "liveness": 0.3,
        "loudness": -5.2,
        "mode": 1,
        "speechiness": 0.05,
        "tempo": 120.0,
        "time_signature": 4,
        "track_href": "https://api.spotify.com/v1/tracks/track_id",
        "type": "audio_features",
        "uri": "spotify:track:track_id",
        "valence": 0.9
    }

    features = AudioFeatures(**valid_data)
    assert features.danceability == 0.8

def test_invalid_danceability():
    invalid_data = {
        "acousticness": 0.5,
        "analysis_url": "https://api.spotify.com/v1/audio-analysis/track_id",
        "danceability": 1.5,  # INVALID
        "duration_ms": 210000,
        "energy": 0.7,
        "id": "track_id",
        "instrumentalness": 0.0,
        "key": 5,
        "liveness": 0.3,
        "loudness": -5.2,
        "mode": 1,
        "speechiness": 0.05,
        "tempo": 120.0,
        "time_signature": 4,
        "track_href": "https://api.spotify.com/v1/tracks/track_id",
        "type": "audio_features",
        "uri": "spotify:track:track_id",
        "valence": 0.9
    }

    with pytest.raises(ValueError, match="Value 1.5 must be between 0.0 and 1.0"):
        AudioFeatures(**invalid_data)

def test_invalid_key():
    invalid_data = {
        "acousticness": 0.5,
        "analysis_url": "https://api.spotify.com/v1/audio-analysis/track_id",
        "danceability": 0.8,
        "duration_ms": 210000,
        "energy": 0.7,
        "id": "track_id",
        "instrumentalness": 0.0,
        "key": 12, # INVALID
        "liveness": 0.3,
        "loudness": -5.2,
        "mode": 1,
        "speechiness": 0.05,
        "tempo": 120.0,
        "time_signature": 4,
        "track_href": "https://api.spotify.com/v1/tracks/track_id",
        "type": "audio_features",
        "uri": "spotify:track:track_id",
        "valence": 0.9
    }

    with pytest.raises(ValueError, match="Key 12 must be between -1 and 11"):
        AudioFeatures(**invalid_data)

def test_invalid_type():
    invalid_data = {
        "acousticness": 0.5,
        "analysis_url": "https://api.spotify.com/v1/audio-analysis/track_id",
        "danceability": 0.8,
        "duration_ms": 210000,
        "energy": 0.7,
        "id": "track_id",
        "instrumentalness": 0.0,
        "key": 5,
        "liveness": 0.3,
        "loudness": -5.2,
        "mode": 1,
        "speechiness": 0.05,
        "tempo": 120.0,
        "time_signature": 4,
        "track_href": "https://api.spotify.com/v1/tracks/track_id",
        "type": "invalid_type", # INVALID
        "uri": "spotify:track:track_id",
        "valence": 0.9
    }

    with pytest.raises(ValueError, match='Type invalid_type must be "audio_features"'):
        AudioFeatures(**invalid_data)
