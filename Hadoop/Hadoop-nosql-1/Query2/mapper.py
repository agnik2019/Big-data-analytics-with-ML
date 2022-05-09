# Agnik Saha
# Roll: 21CS60A01
# Query 2
import sys
def openfile():
    try:
        file=open("network.txt",'r')
    except:
        print("File Does not exist")
        sys.exit()
    return file

file=openfile()
for line in file:
    try:
        line=line.strip()  # removing space
        temp=line.split(" ") # split by space
        node1=temp[0]   # node1 which is sender
        node2=temp[1]   # node 2 which is receiver
        print(node1+","+str(1)) # sender with count
    except Exception as e:
        continue
file.close()


