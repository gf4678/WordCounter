import glob
from janome.tokenizer import Tokenizer
from operator import itemgetter
# from MeCab import Tagger

t = Tokenizer()
# mecab = Tagger("-Ochasen")


def importLyric(dirname): #指定されたディレクトリから歌詞を取得
    dirname += "/*.txt"
    lyrics = []
    lyric_file = glob.glob(dirname)
    # # print(lyric_file, flush=True)

    for j in lyric_file:
        with open(j, mode='r', encoding="utf-8") as f:
            lyrics.append(f.read())
    return lyrics


def countWord(lyrics): #品詞を問わず単語の数をカウント
    words = {}
    for lyric in lyrics:
        # print(i)
        lines = lyric.split("\n")
        wakati = []
        for line in lines:
            wakati.extend(list(t.tokenize(line, wakati=True)))
        # node = mecab.parseToNode(i)
        for j in range(len(wakati)):
            if wakati[j] not in words:
                words[wakati[j]] = 0
            words[wakati[j]] += 1
    return words


def countWordTrucks(lyrics): #品詞を問わず単語の数をカウント
    words = {}
    for lyric in lyrics:
        # print(i)
        lines = lyric.split("\n")
        wakati = []
        for line in lines:
            wakati.extend(list(t.tokenize(line, wakati=True)))
        # node = mecab.parseToNode(i)
        for j in range(len(wakati)):
            if wakati[j] not in words:
                words[wakati[j]] = 0
            if j == 0 or wakati[j] not in wakati[:j-1]:
                words[wakati[j]] += 1
    return words


def countNoun(lyrics): #品詞を指定して単語の数をカウント
    words = {}
    for lyric in lyrics:
        # print(i)
        lines = lyric.split("\n")
        wakati = []
        for line in lines:
            wakati.extend(t.tokenize(line))
        # node = mecab.parseToNode(i)
        # print(wakati)
        thisWords = []
        for word in wakati:
            # print(word)
            if "名詞" in word.part_of_speech:
                if word.surface not in words:
                    words[word.surface] = 0
                words[word.surface] += 1
            thisWords.append(word.surface)
    return words


def countNounTrucks(lyrics): #品詞を指定して単語の数をカウント
    words = {}
    for lyric in lyrics:
        # print(i)
        lines = lyric.split("\n")
        wakati = []
        for line in lines:
            wakati.extend(t.tokenize(line))
        # node = mecab.parseToNode(i)
        # print(wakati)
        thisWords = []
        for word in wakati:
            # print(word)
            if "名詞" in word.part_of_speech:
                if word.surface not in words:
                    words[word.surface] = 0
                if word.surface not in thisWords:
                    words[word.surface] += 1
            thisWords.append(word.surface)
    return words


word = countNounTrucks(importLyric("amazarashi"))
word = sorted(word.items(), key=itemgetter(1))
word.reverse()
word = word[:100]
for i in word:
    # print(i)
    # print(word[i])
    print(str(i[0])+"："+str(i[1]))





