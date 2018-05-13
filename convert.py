import os

start_dir = os.path.join(os.getcwd(), 'sounds')

files = []

for dirpath, dirname, dirfiles in os.walk(start_dir):
    files.extend([os.path.join(dirpath, dirfile) for dirfile in dirfiles])

for f in files:
    #sound = pydub.AudioSegment.from_wav(wavefile)
    #sound.export(wavefile[:-3] + 'mp3', format="mp3")
    #print(wavefile[:-3] + 'mp3')
    if f[-3:] == 'wav':
        os.remove(f)