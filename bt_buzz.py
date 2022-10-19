import os
import time
import logging

import vlc


os.system('amixer controls')

logging.basicConfig(filename='/home/andrew/scripts/logs/hallo.log',
                    format='%(asctime)s, %(module)s, %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8',
                    level=logging.DEBUG)


def play_sound():
    vol = 60
    os.system(f'amixer cset numid=1 {vol}%')
    player = vlc.MediaPlayer(f'/home/andrew/Music/thunder0.mp3')
    player.play()
    time.sleep(0.5)
    duration = player.get_length()
    if duration > 30:
        time.sleep(30)
    else:
        time.sleep(duration)
    player.stop()


if __name__ == '__main__':
    logging.info(f'bt_buzz in')
    play_sound()
    logging.info(f'bt_buzz out')
