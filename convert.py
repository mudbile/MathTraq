import os
import pydub

start_dir = os.path.join(os.getcwd(), 'sounds')

files = []

for dirpath, dirname, dirfiles in os.walk(start_dir):
    files.extend([os.path.join(dirpath, dirfile) for dirfile in dirfiles])

for f in files:
    if f[-3:] == 'mp3':
        sound = pydub.AudioSegment.from_mp3(f)
        print(f)
        os.remove(f)
        sound.export(f[:-3] + 'mp3', format="mp3")
        
    