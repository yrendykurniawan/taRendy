import codecs
import sys
from googletrans import Translator

if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

class Baca:
    def insert_data(self, isidata):
        list1 = []
        translator = Translator()
        translations = translator.translate([isidata], dest='id')
        for translation in translations:
            list1.append(translation.text)

        lokasiFile = '../../dataset/nrc/asli/sinonim/translate/surprise.txt'
        f = open(lokasiFile, 'a', encoding='utf-8')

        f.write(list1[0] + '\n')

        f.close()

        return True

    def write_data(self):
        lokasiFile = '../../dataset/nrc/asli/sinonim/sortkembar/surprise.txt'

        creds = [cred.strip() for cred in open(lokasiFile).readlines()]
        for cred in creds:
            created = self.insert_data(cred)
            if created:
                print(cred)

if __name__ == "__main__":
    s = Baca()
    s.write_data()
