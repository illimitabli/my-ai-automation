from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1-hd",
  voice="alloy",

  input="Jamais la psychologie ne pourra dire sur la folie la vérité, puisque c'est la folie qui détient la vérité de la psychologie."
)
response.stream_to_file(speech_file_path)
