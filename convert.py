import os
import pydub

start_dir = os.path.join(os.getcwd(), 'sounds')

wavefiles = []

for dirpath, dirname, dirfiles in os.walk(start_dir):
    wavefiles.extend([os.path.join(dirpath, dirfile) for dirfile in dirfiles])

print(wavefiles)

for wavefile in wavefiles:
    sound = pydub.AudioSegment.from_wav(wavefile)
    sound.export(wavefile[:-3] + 'mp3', format="mp3")
    print(wavefile[:-3] + 'mp3')