import dotenv
import os
from dataclasses import dataclass, field
from groq import Groq
from pytubefix import Buffer, YouTube
from utils import extract_yt_id

dotenv.load_dotenv()


@dataclass
class Transcriber:
    url: str
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
        buffer = Buffer()
        buffer.download_in_buffer(self.audio_stream)

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        transcription = client.audio.transcriptions.create(
            file=(f"{self.video_id}.mp4", buffer.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
            temperature=0.0,
        )

        return "\n".join(segment["text"] for segment in transcription.segments)


if __name__ == "__main__":
    # no transcript
    url = "https://youtube.com/shorts/K8oHmlacaxk?si=pvf1lx47f8CL34ms"
    print(Transcriber(url).transcript)
