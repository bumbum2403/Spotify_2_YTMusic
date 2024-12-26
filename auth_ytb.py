import os
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load environment variables from the .env file
load_dotenv()

def authenticate_youtube():
    """
    Authenticate with YouTube using OAuth 2.0.
    Returns an authenticated YouTube client.
    """
    client_id = os.getenv("YOUTUBE_CLIENT_ID")
    client_secret = os.getenv("YOUTUBE_CLIENT_SECRET")
    redirect_uri = os.getenv("YOUTUBE_REDIRECT_URI")
    
    # YouTube OAuth flow
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', scopes=scopes
    )
    credentials = flow.run_local_server(port=8080)  # Adjust port as needed

    youtube = build("youtube", "v3", credentials=credentials)
    print("YouTube authentication successful.")
    return youtube
