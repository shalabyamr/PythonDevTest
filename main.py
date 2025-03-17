from image_processor import ImageReader
from video_processor import create_video
from subtitles_processor import text_to_srt, add_subtitles
from voiceover_processor import text_file_to_speech, add_voiceover_to_video

my_image = ImageReader()
my_image.read_image(image_path='./images/statistics.jpg')
my_image.draw_text(text="Statistics and Machine Learning")
my_image.convert_to_greyscale()
subtitles_duration = text_to_srt(input_text_file="./subtitles/speech_content.txt",
                                 output_srt_file="./subtitles/subtitles.srt", duration_per_line=3)
create_video(image_path="./images/out.jpg", audio_path="./audio/go-beyond.mp3", output_video="./videos/out.mp4",
             duration=subtitles_duration, fps=30)
add_subtitles(input_video="./videos/out.mp4", subtitle_file="./subtitles/subtitles.srt",
              output_video="./videos/out_captions.mp4")

text_file_to_speech(txt_file="./subtitles/speech_content.txt", output_audio="./voice/voiceover.mp3")
add_voiceover_to_video(input_video="./videos/out_captions.mp4", voiceover_audio="./voice/voiceover.mp3",output_video="./videos/out_voice_over.mp4")