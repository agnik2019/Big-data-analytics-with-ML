# Agnik Saha
# Roll: 21CS60A01
# Query 4
import sys

# Reading both the file and sending 
file1 = open("network.txt",'r')
file2 = open("dept_labels.txt",'r')

try:
    for line in file1:                          # reading file line by line
        line = line.strip()                    
        words = line.split()                    
        print('%s\t%s\t%s' % (words[0], words[1],'Net'))    # sending to console as key value pair

    for line in file2:
        line = line.strip()
        words = line.split()
        print('%s\t%s\t%s' % (words[0], words[1],'Dept'))  # node_id, dept_id
except:
    print("Error in opening the file")