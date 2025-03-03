import pytest
from youtube_transcript_api import TranscriptsDisabled
from yt_transcribe.utils import extract_yt_id, list_available_languages


@pytest.mark.parametrize(
    "url, expected_id",
    [
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/watch?v=p8mKW2YZt2s&t=388s", "p8mKW2YZt2s"),
        ("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://youtu.be/p8mKW2YZt2s?si=Dhzx8Cx42-H74OwO", "p8mKW2YZt2s"),
        ("https://youtu.be/p8mKW2YZt2s?si=HPOAtUIN3-_FAgqh&t=415", "p8mKW2YZt2s"),
        ("https://www.youtube.com/embed/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/shorts/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://youtube.com/shorts/yJDznRKtzNs?si=BvTazUevs2ezOcJw", "yJDznRKtzNs"),
        ("https://m.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("dQw4w9WgXcQ", None),
        ("not a url", None),
        ("", None),
    ],
)
def test_extract_yt_id(url: str, expected_id: str | None) -> None:
    assert extract_yt_id(url) == expected_id


def test_list_available_languages() -> None:
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert list_available_languages(url) == ["en"]


def test_list_available_languages_no_transcript() -> None:
    url = "https://youtu.be/wE9rpaXtKuc?si=91TL0mjMOTcWEWBO"
    with pytest.raises(TranscriptsDisabled):
        list_available_languages(url)
