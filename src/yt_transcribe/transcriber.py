"""transcribe video with whisper from Groq"""

import dotenv
import os
from dataclasses import dataclass, field
from groq import Groq
from pytubefix import Buffer, YouTube
from yt_transcribe.utils import extract_yt_id

dotenv.load_dotenv()


@dataclass
class Transcriber:
    url: str
    lang: str | None = None
    video_id: str = field(init=False)
    yt: YouTube = field(init=False)

    def __post_init__(self):
        self.video_id = extract_yt_id(self.url)
        self.yt = YouTube(self.url)

    @property
    def audio_stream(self):
        streams = self.yt.streams
        return streams.get_audio_only()

    @property
    def transcript(self) -> str:
        """
        Transcribe the audio of the YouTube video.

        Args:
            lang (str | None): The language of the transcription.
            None for auto-detect language, possible values such as "en", "zh", "yue" ... etc.
            see Groq API `client.audio.transcriptions.create` for more details.
        Returns:
            str: The transcription of the audio.
        """
        buffer = Buffer()
        buffer.download_in_buffer(self.audio_stream)

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        params = dict(
            file=(f"{self.video_id}.mp4", buffer.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
            temperature=0.0,
        )
        if self.lang is not None:
            params["language"] = self.lang
        transcription = client.audio.transcriptions.create(**params)

        return "\n".join(segment["text"] for segment in transcription.segments)


if __name__ == "__main__":
    # no transcript
    url = "https://youtube.com/shorts/K8oHmlacaxk?si=pvf1lx47f8CL34ms"
    print(Transcriber(url).transcript)
