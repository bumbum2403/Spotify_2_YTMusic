def create_youtube_playlist(youtube, title, description):
    """
    Create a new YouTube playlist.
    Args:
        youtube: YouTube API client instance.
        title: Playlist title.
        description: Playlist description.
    Returns:
        Created playlist object.
    """
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["Spotify", "YouTube", "Music"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"  # Set to 'public' if needed
            }
        }
    )
    return request.execute()

def search_youtube_for_video(youtube, query):
    """
    Search for a video on YouTube using a query string.
    Args:
        youtube: YouTube API client instance.
        query: Search query string.
    Returns:
        Video ID of the first search result or None if no results.
    """
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=1
    )
    response = request.execute()
    if "items" in response and len(response["items"]) > 0:
        return response["items"][0]["id"]["videoId"]
    return None

def add_song_to_youtube_playlist(youtube, playlist_id, video_id):
    """
    Add a video to a YouTube playlist.
    Args:
        youtube: YouTube API client instance.
        playlist_id: ID of the YouTube playlist.
        video_id: ID of the YouTube video to add.
    """
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    request.execute()
