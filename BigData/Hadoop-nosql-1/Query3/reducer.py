# Agnik Saha
# Roll: 21CS60A01
# Query 3
from operator import itemgetter
import sys

def top_10_employee():
    try:
        file2=open("../Query2/result.txt",'r')
    except:
        print("task 2 result file does not exist")
        sys.exit()
    top_10=[]
    for line in file2:
        line=line.strip()
        top_10.append(line)
    file2.close()
    return top_10



top_10 = top_10_employee() # returns list of top 10 employees
top_dict = {} # dictionary of list

# initialization of dictionary
for item in top_10:
    top_dict[item] = list()

  
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    sender, receiver = line.split('\t')

    if receiver in top_10:
        #print(f"{sender} and receiver {receiver}")
        top_dict[receiver].append(sender)
# printing  the values of top_dict
for key in top_dict:
    print(f'{key} {len(top_dict[key])}') 
 
