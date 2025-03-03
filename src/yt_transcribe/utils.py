from urllib.parse import parse_qs, urlparse
from youtube_transcript_api import Transcript, YouTubeTranscriptApi


def extract_yt_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.

    Args:
        youtube_url (str): The YouTube URL.

    Returns:
        str or None: The video ID, or None if not found.
    """
    try:
        parsed_url = urlparse(youtube_url)
        if parsed_url.hostname in (
            "www.youtube.com",
            "youtube.com",
            "m.youtube.com",
            "youtu.be",
        ):
            if parsed_url.hostname in (
                "www.youtube.com",
                "youtube.com",
                "m.youtube.com",
            ):
                if parsed_url.path == "/watch":
                    query_params = parse_qs(parsed_url.query)
                    video_id = query_params.get("v")
                    if video_id:
                        return video_id[0]
                elif parsed_url.path.startswith("/embed/"):
                    return parsed_url.path.split("/")[2]
                elif parsed_url.path.startswith("/shorts/"):
                    return parsed_url.path.split("/")[2]
            elif parsed_url.hostname == "youtu.be":
                return parsed_url.path[1:]  # remove leading slash
    except Exception:
        return None
    return None


def list_available_languages(url: str) -> list[str]:
    """
    Lists all available languages for a given YouTube video.

    Args:
        url (str): The URL of the YouTube video.

    Returns:
        list[str]: A list of available languages.
    """
    video_id = extract_yt_id(url)
    return [
        transcript.language_code
        for transcript in YouTubeTranscriptApi.list_transcripts(video_id)
    ]


if __name__ == "__main__":
    print(list_available_languages("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
