from image_processor import ImageReader

my_image = ImageReader()

my_image.read_image(image_path='./images/statistics.jpg')

my_image.draw_text(text="Statistics and Machine Learning")

my_image.convert_to_greyscale()

my_image.text_to_srt(input_text_file="./subtitles/speech_content.txt",
                     output_srt_file="./subtitles/subtitles.srt", duration_per_line=3)

my_image.text_file_to_speech(txt_file="./subtitles/speech_content.txt",
                             output_audio="./voice/voiceover.mp3", lang="en")

my_image.create_video(image_path="./images/out.jpg", audio_path="./audio/go-beyond.mp3",
                      output_video="./videos/out.mp4",
                      duration=my_image.voice_over_duration, fps=30)

my_image.add_subtitles(input_video="./videos/out.mp4", subtitle_file="./subtitles/subtitles.srt",
                       output_video="./videos/out_captions.mp4")


my_image.add_voiceover_to_video(input_video="./videos/out_captions.mp4",
                                narration_audio="./voice/voiceover.mp3",
                                original_audio = "./audio/go-beyond.mp3",
                                output_video="./videos/out_voice_over.mp4")

