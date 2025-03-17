import ffmpeg

def create_video(image_path, output_video:str, audio_path:str, duration:int=10, fps:int=30):
                """
                Creates a short video from an image using ffmpeg-python.
                :param image_path:str: Path to the input image
                :param output_video:str: Path to the output video file
                :param audio_path:str: Path to the input audio file
                :param duration:int: Duration of the video in seconds (default: 10 seconds)
                :param fps:int: Frames per second (default: 30 frames per second)
                """
                (
                    ffmpeg
                    .input(image_path, loop=1, t=duration)
                    .filter("scale", 1280, 720)
                    .output(ffmpeg.input(audio_path), output_video, vcodec="libx264", acodec="aac", pix_fmt="yuv420p", r=fps,
                            shortest=None)
                    .run(overwrite_output=True)
                )
                print(f"Video saved as {output_video}")



def add_subtitle(input_video, subtitle_file, output_video):
    """
        Adds hardcoded subtitles to a video.
        This function overlays subtitles onto the video permanently, making them
        always visible (burned-in). It does not create selectable (soft) subtitles.

        Parameters:
        ----------
        input_video : str
            Path to the input video file.
        subtitle_file : str
            Path to the subtitle file (.srt or .ass) to overlay on the video.
        output_video : str
            Path to the output video file with subtitles added.

        Returns:
        -------
        None
            The function processes the video and saves it to the specified output path.

        Example:
        --------
        add_subtitles("input.mp4", "subtitles.srt", "output.mp4")
        """
    (
        ffmpeg
        .input(input_video)
        .filter("subtitles", subtitle_file)
        .output(output_video, c="copy")
        .run(overwrite_output=True)
    )

