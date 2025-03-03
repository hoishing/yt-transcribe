# Youtube Transcript Extract and Transcribe

- `Extractor`: extract transcript from youtube video if available
    - available formats: text, SRT, webVTT

- `Transcriber`: use whisper to transcribe the video if no transcript is available

## Installation

```bash
pip install yt-transcribe
```

Put your `GROQ_API_KEY` in `.env`

## Usage

```python
from yt_transcribe import Extractor, Transcriber

# video with transcript
extractor = Extractor(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print(extractor.transcript)

# video without transcript, use whisper to transcribe
transcriber = Transcriber(url="https://youtube.com/shorts/NbY29sW7gbU?si=EJpsZdXvUArCIBr3")
print(transcriber.transcript)
```
