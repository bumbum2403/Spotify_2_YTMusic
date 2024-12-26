from auth_spotify import authenticate_spotify, get_user_playlists, get_spotify_playlist_tracks
from auth_ytb import authenticate_youtube
from utils import create_youtube_playlist, search_youtube_for_video, add_song_to_youtube_playlist

def main():
    # Authenticate Spotify
    spotify = authenticate_spotify()

    # Authenticate YouTube
    youtube = authenticate_youtube()

    # Get Spotify playlists
    spotify_playlists = get_user_playlists(spotify)
    print("Your Spotify playlists:")
    for idx, playlist in enumerate(spotify_playlists, start=1):
        print(f"{idx}. {playlist['name']} ({playlist['tracks']} tracks)")

    # User selects a playlist
    playlist_index = int(input("Enter the number of the playlist to import: ")) - 1
    spotify_playlist = spotify_playlists[playlist_index]

    # Prompt user for batch size
    batch_size = int(input("Enter the number of tracks to import (e.g., 25): "))

    # Create YouTube playlist
    title = spotify_playlist['name']
    description = f"Imported from Spotify: {spotify_playlist['name']}"
    youtube_playlist = create_youtube_playlist(youtube, title, description)

    print(f"Created YouTube playlist: {youtube_playlist['snippet']['title']}")

    # Get tracks from Spotify and add them to YouTube
    offset = 0
    while True:
        spotify_tracks = get_spotify_playlist_tracks(
            spotify, spotify_playlist['id'], batch_size, offset=offset
        )
        if not spotify_tracks:
            break

        for track in spotify_tracks:
            query = f"{track['name']} {track['artist']}"
            video_id = search_youtube_for_video(youtube, query)
            if video_id:
                add_song_to_youtube_playlist(youtube, youtube_playlist['id'], video_id)

        offset += batch_size
        print(f"Imported {offset} tracks so far...")

    print("Playlist import completed!")

if __name__ == "__main__":
    main()
