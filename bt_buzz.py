import os
import time
import vlc


os.system('amixer controls')


def play_sound():
    vol = 10
    os.system(f'amixer cset numid=1 {vol}%')
    player = vlc.MediaPlayer(f'/home/andrew/Music/thunder0.mp3')
    player.play()
    time.sleep(0.5)
    duration = player.get_length()
    time.sleep(duration)
    player.stop()


if __name__ == '__main__':
    play_sound()
