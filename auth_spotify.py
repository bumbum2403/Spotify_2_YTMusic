import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate_spotify():
    """
    Authenticate with Spotify using OAuth.
    Returns a Spotipy client instance.
    """
    scope = "playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    print("Spotify authentication successful.")
    return sp

def get_user_playlists(spotify):
    """
    Retrieve the user's playlists from Spotify.
    Args:
        spotify: Spotipy client instance.
    Returns:
        List of playlists with their names and IDs.
    """
    playlists = []
    results = spotify.current_user_playlists()
    while results:
        for item in results['items']:
            playlists.append({
                'name': item['name'],
                'id': item['id'],
                'tracks': item['tracks']['total']
            })
        results = spotify.next(results) if results['next'] else None
    return playlists

def get_spotify_playlist_tracks(spotify, playlist_id, batch_size, offset=0):
    """
    Get tracks from a Spotify playlist in batches.
    Args:
        spotify: Spotipy client instance.
        playlist_id: Spotify playlist ID.
        batch_size: Number of tracks to fetch in one batch.
        offset: Starting point for fetching tracks.
    Returns:
        List of track names and artists.
    """
    tracks = []
    results = spotify.playlist_items(playlist_id, limit=batch_size, offset=offset)
    for item in results['items']:
        track = item['track']
        tracks.append({
            'name': track['name'],
            'artist': ', '.join(artist['name'] for artist in track['artists'])
        })
    return tracks
