"""extract transcript from video"""

from dataclasses import dataclass, field
from typing import Literal
from utils import extract_yt_id
from youtube_transcript_api import Transcript, YouTubeTranscriptApi
from youtube_transcript_api.formatters import (
    SRTFormatter,
    TextFormatter,
    WebVTTFormatter,
)


@dataclass
class Extractor:
    url: str
    lang: str
    video_id: str = field(init=False)

    def __post_init__(self):
        self.video_id = extract_yt_id(self.url)

    @property
    def transcript(self) -> Transcript:
        return YouTubeTranscriptApi.get_transcript(self.video_id, languages=[self.lang])

    @property
    def available_langs(self) -> list[str]:
        transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
        return [transcript.language_code for transcript in transcript_list]

    def formatted_transcript(
        self, format: Literal["txt", "webvtt", "srt"] = "txt"
    ) -> str:
        formatter = {
            "txt": TextFormatter(),
            "webvtt": WebVTTFormatter(),
            "srt": SRTFormatter(),
        }[format]

        return formatter.format_transcript(self.transcript)


if __name__ == "__main__":
    # english transcript only
    url = "https://youtube.com/shorts/yJDznRKtzNs?si=2-S99hmZNu2mYfql"
    extractor = Extractor(url=url, lang="en")
    print(extractor.available_langs)
    print(extractor.formatted_transcript())
