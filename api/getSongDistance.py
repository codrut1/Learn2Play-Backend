import librosa
from dtw import dtw
from numpy.linalg import norm

def calculateMFCCscore(path1, path2):
    y1, sr1 = librosa.load(path1)
    y2, sr2 = librosa.load(path2)

    mfcc1 = librosa.feature.mfcc(y1, sr1)
    mfcc2 = librosa.feature.mfcc(y2, sr2)

    dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    return dist
