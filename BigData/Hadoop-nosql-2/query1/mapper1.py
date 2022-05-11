# Name:mapper1.py
# Agnik Saha

import sys

def openfile(inputFileName):
    try:
        file=open(inputFileName,'r')    
    except:
        print("File Does not exist")
        sys.exit()
    return file

#Function to Print output nodes
def mapper():
    #get filename from command line
    inputFileName = sys.argv[1]
    file=openfile(inputFileName)
    for line in file:
        #removing trailing endline and white spaces
        line=line.strip()
        try:
            #split the pair of nodes
            temp=line.split("#")
            node=temp[0]
            node_array=node.split(" ")
            node0=node_array[0]
            node1=node_array[1]
            #if nodes are not of form (x,x) , then send to combiner
            if int(node0)!=int(node1):
                print(node0+","+node1+";"+str(1))
        except Exception as e:
            pass
    file.close()

if __name__ == "__main__":
    mapper()