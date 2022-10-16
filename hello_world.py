import os
import time
import vlc
from multiprocessing import Process

import cam as ca

os.system('amixer controls')


def play_music():
    while(1):
        songs = [s for s in os.listdir('/home/andrew/Music/') if '.mp3' in s]
        for s in songs:
            print(s)
            vol = 80
            if 'vol' in s:
                vol = int(s.split('vol')[1][:3])
            os.system(f'amixer cset numid=1 {vol}%')
            player = vlc.MediaPlayer(f'/home/andrew/Music/{s}')
            player.play()
            time.sleep(0.5)
            duration = player.get_length()
            print(duration)
            time.sleep(duration)


if __name__ == '__main__':
    p = Process(target=ca.start)
    p.start()
    play_music()
    p.join()
