from pydantic import BaseModel, field_validator

__all__ = ['AudioFeatures', 'AudioFeaturesResponse']

class AudioFeatures(BaseModel):
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    track_href: str
    type: str
    uri: str
    valence: float
    
    @field_validator('acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness' , 'valence', mode='before')
    def validate_percentage_fields(cls, value):
        if not 0.0 <= value <= 1.0:
            raise ValueError(f'Value {value} must be between 0.0 and 1.0')
        return value
    
    @field_validator('key', mode='before')
    def validate_key(cls, value):
        if not -1 <= value <= 11:
            raise ValueError(f'Key {value} must be between -1 and 11')
        return value

    @field_validator('loudness', mode='before')
    def validate_loudness(cls, value):
        if not -60.0 <= value <= 0.0:
            raise ValueError(f'Loudness {value} must be between -60.0 and 0.0 dB')
        return value

    @field_validator('time_signature', mode='before')
    def validate_time_signature(cls, value):
        if not 3 <= value <= 7:
            raise ValueError(f'Time signature {value} must be between 3 and 7')
        return value

    @field_validator('type', mode='before')
    def validate_type(cls, value):
        if value != 'audio_features':
            raise ValueError(f'Type {value} must be "audio_features"')
        return value


class AudioFeaturesResponse(BaseModel):
    audio_features: list[AudioFeatures | None]
