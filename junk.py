import ffmpeg
print(round(float(ffmpeg.probe('./voice/voiceover.mp3')['format']['duration']),0))