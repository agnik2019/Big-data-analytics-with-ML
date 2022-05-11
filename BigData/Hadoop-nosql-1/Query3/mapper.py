# Agnik Saha
# Roll: 21CS60A01
# Query 3
import sys

# Reading from network.txt
for line in sys.stdin:
    # remove spaces
    line = line.strip()
    # split lines by space
    words = line.split()
    print('%s\t%s' % (words[0],words[1]))