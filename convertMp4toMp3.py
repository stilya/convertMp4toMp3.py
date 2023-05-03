# pip install moviepy или pip install moviepy
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Директория, в которой находятся видеофайлы
input_dir = "/video"
# Директория, в которую нужно сохранить аудиофайлы
output_dir = "/mp3"

# Проходим по всем видеофайлам в директории и конвертируем их в аудиофайлы
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".mp4"):
            # Определяем путь к видеофайлу и аудиофайлу
            video_path = os.path.join(root, file)
            audio_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".mp3")
            # Конвертируем видеофайл в аудиофайл
            video_clip = VideoFileClip(video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_path)
            # Очищаем временные файлы
            audio_clip.close()
            video_clip.close()

print("Конвертация завершена!")