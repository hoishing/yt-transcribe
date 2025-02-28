from urllib.parse import parse_qs, urlparse


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
