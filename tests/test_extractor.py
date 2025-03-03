import pytest
from yt_transcribe.extractor import Extractor
from youtube_transcript_api import NoTranscriptFound, TranscriptsDisabled


@pytest.fixture
def no_transcript():
    return "https://youtube.com/shorts/NbY29sW7gbU?si=EJpsZdXvUArCIBr3"


@pytest.fixture
def english_transcript():
    return "https://youtube.com/shorts/yJDznRKtzNs?si=2-S99hmZNu2mYfql"


def test_no_transcript(no_transcript: str):
    with pytest.raises(TranscriptsDisabled):
        Extractor(no_transcript, "en").transcript


def test_english_transcript(english_transcript: str):
    extractor = Extractor(english_transcript, "en")
    assert extractor.transcript is not None


def test_lang_not_available(english_transcript: str):
    extractor = Extractor(english_transcript, "fr")
    with pytest.raises(NoTranscriptFound):
        extractor.transcript
