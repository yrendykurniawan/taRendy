import os
from nltk.corpus import wordnet

workindDir = os.getcwd()


def getSyn(str):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(str):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return synonyms

lokasiFile = workindDir + '//dataset//nrc//asli//SURPRISE_WORDS.txt'

creds = [cred.strip() for cred in open(lokasiFile).readlines()]

for cred in creds:
    lokasiFileTulis = workindDir + '//dataset//nrc//asli//sinonim//surprise.txt'
    f = open(lokasiFileTulis, 'a', encoding='utf-8')
    f.write(cred + '\n')
    f.close()

    dataku = getSyn(cred)
    for credx in dataku:
        lokasiFileTulis = workindDir + '//dataset//nrc//asli//sinonim//surprise.txt'
        f = open(lokasiFileTulis, 'a', encoding='utf-8')
        f.write(credx + '\n')
        f.close()
        print(credx)

print(workindDir)