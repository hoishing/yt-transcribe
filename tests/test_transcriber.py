import pytest
from transcriber import Transcriber


@pytest.fixture
def transcriber():
    return Transcriber("https://youtube.com/shorts/K8oHmlacaxk?si=pvf1lx47f8CL34ms")


def test_transcriber(transcriber: Transcriber):
    assert "通訊軟體" in transcriber.transcript
