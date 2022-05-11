# Agnik Saha
# Roll: 21CS60A01
# Query 4

from operator import itemgetter
import sys
import operator


net = []
dept_dict = {}
outgoing_mails = {}

for i in range(0,42):
    outgoing_mails[i] = 0


# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    word, word1, data = line.split('\t')
    if data.strip() == 'Net':         
        net.append(line)
    else:   
        dept_dict[word] = word1 # dictionary 


# print(dept_dict)
for line in net:
    line = line.strip()
    sender, receiver, data = line.split('\t')
    if dept_dict[sender] != dept_dict[receiver]: 
        outgoing_mails[int(dept_dict[sender])] = outgoing_mails[int(dept_dict[sender])] +1



max_key = max(outgoing_mails, key= lambda x: outgoing_mails[x])
print(f'{max_key} {outgoing_mails[max_key]}')