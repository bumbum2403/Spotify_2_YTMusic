
# Spotify to YouTube Music Playlist Importer

A Python script that allows you to import your Spotify playlists into YouTube Music using their respective APIs.

## Features

- **Spotify Playlist Extraction**: Retrieve playlists from Spotify.
- **YouTube Music Playlist Creation**: Create and add songs to a playlist on YouTube Music.
- **Easy Setup**: Simple configuration with API keys stored in a `.env` file for security.

## Requirements

- Python 3.x
- You will need to install the following Python libraries:
  - `spotipy` (for interacting with Spotify's API)
  - `google-api-python-client` (for interacting with YouTube Music's API)
  - `python-dotenv` (for loading environment variables)

## Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/bumbum2403/Spotify_2_YTMusic
   cd spotify-to-youtube-music
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root:**

   Add your Spotify and YouTube API credentials in the `.env` file.

   Example `.env` file:
   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

5. **Run the script:**
   ```bash
   python main.py
   ```

## Usage

- The script will authenticate with Spotify and YouTube Music using the API keys provided in the `.env` file.
- It will prompt you to log into your Spotify account to select a playlist.
- After choosing the playlist, the script will create a new playlist in YouTube Music and import the songs.

## Contributing

Feel free to fork the repository, make improvements, and create pull requests. For any issues or bugs, please open an issue on GitHub.


## Acknowledgments

- [Spotipy](https://github.com/plamere/spotipy) for Spotify API integration.
- [Google API Python Client](https://github.com/googleapis/google-api-python-client) for YouTube Music API integration.
