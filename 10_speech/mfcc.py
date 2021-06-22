import librosa
import pickle

def getfv(path):
    y, sr = librosa.load(path=path, sr=8000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    fv = []
    for x in (mfcc):
        s = int(sum(x)/len(x))
        fv.append(s)
    return fv

files = ['insert file paths for audio samples']
fvs = [None, None] #initialize to size = number of audio samples

fv = getfv(files[0])
fvs[0]=fv
fv = getfv(files[1])
fvs[1]=fv

open_file = open('features', "wb")
pickle.dump(fvs, open_file)
open_file.close()