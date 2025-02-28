import pytest
from utils import extract_yt_id


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
