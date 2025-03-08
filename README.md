# Youtube Transcript Extract and Transcribe

This package provides a simple way to extract and transcribe Youtube videos.

- If transcript is available, you can use `Extractor` to get the transcript.
- If no transcript is disabled, you can use `Transcriber` to transcribe the video with Whisper from Groq.

## Installation

```bash
pip install yt-transcribe
```

Put your `GROQ_API_KEY` in `.env`

## Usage

```python
from yt_transcribe import Extractor, Transcriber, list_available_languages

# list available transcript languages for a video
list_available_languages("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # ["en"]

# raise `TranscriptsDisabled` for a video disabled transcript
list_available_languages("https://youtube.com/shorts/NbY29sW7gbU?si=EJpsZdXvUArCIBr3") # raise

# video with transcript
extractor = Extractor(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", lang="en")
print(extractor.formatted_transcript(format="srt"))  # format: srt, txt, webvtt

# video without transcript, use whisper to transcribe
transcriber = Transcriber(url="https://youtube.com/shorts/NbY29sW7gbU?si=EJpsZdXvUArCIBr3")
print(transcriber.transcript)

# video without transcript, specify language to enhance accuracy
transcriber = Transcriber(url="https://youtube.com/shorts/NbY29sW7gbU?si=EJpsZdXvUArCIBr3", lang="zh")
print(transcriber.transcript)
```
