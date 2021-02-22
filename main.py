import glob
from janome.tokenizer import Tokenizer
from operator import itemgetter
# from MeCab import Tagger

t = Tokenizer()
# mecab = Tagger("-Ochasen")
def importLyric(dirname):
    dirname += "/*.txt"
    lyrics = []
    lyric_file = glob.glob(dirname)
    # # print(lyric_file, flush=True)

    for j in lyric_file:
        with open(j, mode='r', encoding="utf-8") as f:
            lyrics.append(f.read())
    return lyrics


def analysis(lyrics):
    word = {}
    for lyric in lyrics:
        # print(i)
        lines = lyric.split("\n")
        wakati = []
        for line in lines:
            wakati.extend(list(t.tokenize(line, wakati=True)))
        # node = mecab.parseToNode(i)
        for j in range(len(wakati)):
            if wakati[j] not in word:
                word[wakati[j]] = 0
            if j == 0 or wakati[j] not in wakati[:j-1]:
                word[wakati[j]] += 1
    return word


word = analysis(importLyric("amazarashi"))
word = sorted(word.items(), key=itemgetter(1))
word.reverse()
word = word[:100]
for i in word:
    # print(i)
    # print(word[i])
    print(str(i[0])+"："+str(i[1]))





