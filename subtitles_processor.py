from datetime import timedelta
import ffmpeg

def format_time(td):
    """
    Converts a timedelta object to SRT timestamp format (HH:MM:SS,mmm).
    """
    total_seconds = int(td.total_seconds())
    milliseconds = int(td.microseconds / 1000)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def text_to_srt(**kwargs):
    """
    Reads a text file and converts its content into an .srt subtitle file.

    Parameters:
    -----------
    input_text_file : str
        Path to the input text file containing the content.
    output_srt_file : str
        Path to the output .srt subtitle file.
    duration_per_line : int, optional
        Duration (in seconds) each subtitle should be displayed (default is 3 seconds).

    Returns:
    --------
        - Total Runtime Duration (in seconds) to allocate video total runtime plus an added 3 seconds for
           future credits implementation.
        - Creates an .srt file with the generated subtitles.
    """
    try:
        with open(file=kwargs['input_text_file'], mode="r", encoding="utf-8") as file:
            text = file.read()

        lines = text.split(". ")  # Split into sentences
        subtitles = []
        current_time = timedelta(0)  # Start at 00:00:00,000
        for i, line in enumerate(lines, start=1):
            start = format_time(current_time)
            current_time += timedelta(seconds=kwargs['duration_per_line'])
            end = format_time(current_time)

            subtitle_entry = (
                f"{i}\n"
                f"{start} --> {end}\n"
                f"{line.strip()}.\n\n"
            )

            subtitles.append(subtitle_entry)

        with open(file=kwargs['output_srt_file'], mode="w", encoding="utf-8") as f:
            f.writelines(subtitles)

        print(f"Subtitle file saved as {kwargs['output_srt_file']}")

    except Exception as e:
        print(f"Error: {e}")



def add_subtitles(**kwargs):
    """
    Adds hardcoded subtitles to a video using FFmpeg.

    Parameters:
    -----------
    input_video : str
        Path to the input video file.
    subtitle_file : str
        Path to the subtitle file (e.g., .srt).
    output_video : str
        Path to the output video file with subtitles.

    Returns:
    --------
    None
        Saves the output video with hardcoded subtitles.
    """
    try:
        (
            ffmpeg
            .input(kwargs['input_video'])
            .output(kwargs['output_video'], vf=f"subtitles={kwargs['subtitle_file']}", vcodec="libx264", acodec="aac")
            .run(overwrite_output=True)
        )
        print(f"Video saved with subtitles: {kwargs['output_video']}")
    except Exception as e:
        print(f"An error occurred: {e}")

