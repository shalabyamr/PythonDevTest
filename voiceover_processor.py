from gtts import gTTS
import ffmpeg

def text_file_to_speech(txt_file, output_audio="./voice/voiceover.mp3", lang="en"):
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
        with open(txt_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Convert text to speech
        tts = gTTS(text, lang=lang)

        tts.save(output_audio)
        print(f"Speech saved as: {output_audio}")
    except Exception as e:
        print(f"Error: {e}")



import ffmpeg

def add_voiceover_to_video(input_video, voiceover_audio, output_video):
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
        video = ffmpeg.input(input_video)
        original_audio = ffmpeg.input(voiceover_audio)
        narration_audio = ffmpeg.input(voiceover_audio).audio
        mixed_audio = ffmpeg.filter([original_audio, narration_audio], 'amix', inputs=2, duration='first', dropout_transition=0)

        # Merge audio with video (replacing original audio)
        (
            ffmpeg
            .output(video, mixed_audio, output_video, vcodec="libx264", acodec="aac", strict="experimental")
            .run(overwrite_output=True)
        )

        print(f"Video with voiceover saved as: {output_video}")

    except Exception as e:
        print(f"Error: {e}")
