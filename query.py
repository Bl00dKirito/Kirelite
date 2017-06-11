import sys
import subprocess

from core.profile.loader import loadProfile
from core.tts import tts
from core.stt import stt
from core.brain import query


def main():
    data = loadProfile()
    tts('Welcome ' + data['name'] +
        ', how can I help you?')

    while True:
        if sys.platform == 'darwin':
            subprocess.call(['afplay', 'data/snowboy_resources/ding.wav'])
        elif sys.platform.startswith('linux') or sys.platform == 'win32':
            subprocess.call(['mpg123', 'data/snowboy_resources/ding.wav'])

        text = stt()

        if text is None:
            continue
        else:
            query(text)

if __name__ == "__main__":
    main()
