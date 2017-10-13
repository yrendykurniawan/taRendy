import sqlite3
from tqdm import *


class Baca:
    def create_sql(self, post_id):
        # connect to database
        conn = sqlite3.connect('../../dataset/nrc/asli/sinonim/translate/'+ post_id + '.db')
        c = conn.cursor()

        # Create table

        c.execute(
            "CREATE TABLE IF NOT EXISTS dataku(comment_id INTEGER PRIMARY KEY,"
            "data_komen TEXT,"
            "emosi TEXT)")


        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        conn.close()


    def scrape(self, emosi):

        lokasiFile = '../../dataset/nrc/asli/sinonim/translate/'+ emosi + '.txt'

        creds = [cred.strip() for cred in open(lokasiFile).readlines()]
        for cred in creds:
            self.create_sql(emosi)

            conn = sqlite3.connect('../../dataset/nrc/asli/sinonim/translate/' + emosi + '.db')
            c = conn.cursor()


            c.execute("INSERT INTO dataku VALUES(null, ?, ?);", (cred, emosi, ))

            # Save (commit) the changes
            conn.commit()

            # We can also close the connection if we are done with it.
            conn.close()


            print(cred)


if __name__ == "__main__":
    s = Baca()
    s.scrape('surprise')
