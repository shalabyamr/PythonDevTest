from gtts import gTTS
import ffmpeg

def text_file_to_speech(**kwargs):
    """
    Converts a text file to speech using Google Text-to-Speech (gTTS).

    Parameters:
    -----------
    txt_file : str
        Path to the input text file.
    output_audio : str
        Path to save the generated speech file.
    lang : str
        Language code for speech synthesis.

    Returns:
    --------
    None
        Saves the generated speech as an MP3 file.
    """
    try:
        # Read the text file
        with open(file=kwargs['txt_file'], mode="r", encoding="utf-8") as file:
            text = file.read()

        # Convert text to speech
        tts = gTTS(text, lang=kwargs['lang'])

        tts.save(kwargs['output_audio'])
        print(f"\n*****\nText {kwargs['txt_file']}-to-Speech saved as: {kwargs['output_audio']}\n*****")
        mp3_duration = int(round(float(ffmpeg.probe(kwargs['output_audio'])['format']['duration']), 0))
        print(f"Duration oft the MP3 [ Voice Over ] File is: {mp3_duration}\n********\n")
        return mp3_duration
    except Exception as e:
        print(f"Error: {e}")


def add_voiceover_to_video(**kwargs):
    """
    Merges a video with a voice-over (narration) audio file.

    Parameters:
    -----------
    input_video : str
        Path to the input video file.
    voiceover_audio : str
        Path to the voice-over (narration) audio file (MP3 or WAV).
    output_video : str
        Path to the output video file with added narration.

    Returns:
    --------
    None
        Saves the output video with the voice-over.
    """
    try:
        # Load input video and narration audio
        video = ffmpeg.input(kwargs['input_video'])
        original_audio = ffmpeg.input(kwargs['original_audio'])
        narration_audio = ffmpeg.input(kwargs['narration_audio'])
        # Mix audio properly
        mixed_audio = ffmpeg.filter([original_audio.audio, narration_audio.audio], 'amix', duration='first')

        # Output the mixed audio
        output = ffmpeg.output(mixed_audio, "./audio/mixed_audio.mp3")
        output.run(overwrite_output=True)
        (
            ffmpeg
            .output(video, mixed_audio, kwargs['output_video'], vcodec="libx264", acodec="aac", strict="experimental")
            .run(overwrite_output=True)
        )

        print(f"Video with voiceover saved as: {kwargs['output_video']}")

    except Exception as e:
        print(f"Error: {e}")
