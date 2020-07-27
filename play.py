import time
from pygame import mixer

def play_music(soundfile, duration):

    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(loops=-1)
    time.sleep(duration)

play_music("audio.mp3", 0)