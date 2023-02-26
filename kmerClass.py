import sqlite3
import sys


con = sqlite3.connect("dbtemp.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS kmer(seq, count)")


f = open("temp.thom", "r")
opf = open("opfile.csv", "w")


for line in f:
	if cur.execute(f"SELECT EXISTS (SELECT * FROM kmer WHERE seq = '{line.strip()}')").fetchone()[0] == 1:
		cur.execute(f"UPDATE kmer SET count = count + 1 WHERE seq = '{line.strip()}'")
	else:
		cur.execute(f"INSERT INTO kmer VALUES ('{line.strip()}', 1)")


a = cur.execute("SELECT count, COUNT(*) FROM kmer GROUP BY count")

opf.write(f"nrep,nfound\n")
for val in a.fetchall():
  opf.write(f"{val[0]},{val[1]}\n")

f.close()
opf.close()
