import sqlite3
import urllib

conn = sqlite3.connect('counts.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = urllib.urlopen('http://www.pythonlearn.com/code/mbox.txt')

for line in fname:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    org = pieces[1].split('@')[1]
    
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))

# This statement commits outstanding changes to disk each 
# time through the loop - the program can be made faster 
# by moving the commit so it runs only after the loop completes
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()