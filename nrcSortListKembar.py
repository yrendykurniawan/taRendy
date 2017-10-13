import os

workindDir = os.getcwd()

a = []
lokasiFile = workindDir + '//dataset//nrc//asli//sinonim//surprise.txt'

creds = [cred.strip() for cred in open(lokasiFile).readlines()]

for cred in creds:
   a.append(cred)

a = list(set(a))

for hasil in a:
    lokasiFileTulis = workindDir + '//dataset//nrc//asli//sinonim//sortkembar//surprise.txt'
    f = open(lokasiFileTulis, 'a', encoding='utf-8')
    f.write(hasil + '\n')
    f.close()
    print(hasil)
