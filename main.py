import glob
from janome.tokenizer import Tokenizer

t = Tokenizer()
def importLyric(dirname):
    dirname += "/*.txt"
    lyrics = []
    lyric_file = glob.glob(dirname)
    # # print(lyric_file, flush=True)

    for j in lyric_file:
        with open(j, mode='r') as f:
            lyrics.append(f.read())
    return lyrics


def analysis(lyrics):
    word = {}
    for i in lyrics:
        wakati = list(t.tokenize(i, wakati=True))
        for j in range(len(wakati)):
            if wakati[j] not in word:
                word[wakati[j]] = 1
            elif j == 0 or wakati[j] not in wakati[:j-1]:
                word[wakati[j]] += 1
    return word


print(analysis(importLyric("Lyrics")))





