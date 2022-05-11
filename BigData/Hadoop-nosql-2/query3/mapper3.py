
import sys

def openfile(inputFileName):
    try:
        file=open(inputFileName,'r')
    except :
        print("File Network.txt does not exist")
        sys.exit()
    return file
def mapper():

    inputFileName = sys.argv[1]
    file=openfile(inputFileName)
    for line in file:
        line=line.strip()
        try:
            #split the pair of nodes
            nodes=line.split(",")
            node0=nodes[0]
            node1=nodes[1]

            print(node0+","+node1)  # 
        except Exception as e:
            #print(e)
            pass


    file.close()

if __name__ == '__main__':
    mapper()