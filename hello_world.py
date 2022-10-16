import os
import time
import vlc
from multiprocessing import Process
import datetime
import random

import cam as ca

os.system('amixer controls')

def in_between(now, start=datetime.time(16, 30), end=datetime.time(19, 30)):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end


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

def play_sound():
    with open('play_sound_running.txt', 'r+') as f:
        first_line = f.readline()
        if 'running' in first_line:
            return
        else:
            f.write('running')
            f.close()

    songs = [s for s in os.listdir('/home/andrew/Music/') if '.mp3' in s]
    s = random.choice(songs)
    print(s)
    vol = 80
    if 'vol' in s:
        vol = int(s.split('vol')[1][:3])
    os.system(f'amixer cset numid=1 {vol}%')
    player = vlc.MediaPlayer(f'/home/andrew/Music/{s}')
    player.play()
    time.sleep(0.5)
    duration = player.get_length()
    if duration > 30:
        duration = 30
    time.sleep(duration)
    player.stop()

    with open('play_sound_running.txt', 'w') as f:
        f.write('silent')

    return


if __name__ == '__main__':
    p = Process(target=ca.start)
    p.start()
    #play_music()
    p.join()
