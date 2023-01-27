import moviepy.editor
from pathlib import Path


if __name__ == '__main__':
    video_file = Path('your_file_name')

    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    audio.write_audiofile(f'{video_file.stem}.mp3')
