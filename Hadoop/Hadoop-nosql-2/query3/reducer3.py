import sys
# create graph class
class Graph(object):

    def __init__(self, vertices):
        self.adjMatrix = []
        for i in range(vertices):
            self.adjMatrix.append([0 for i in range(vertices)])
        self.vertices = vertices

        # Add edges
    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

       
    
def reducer():
    g = Graph(42) # 42 departments
    for line in sys.stdin:
        line=line.strip()
        nodes=line.split(",")
        node0 = nodes[0]
        node1 = nodes[1]
        g.add_edge(int(node0),int(node1))


    # multiply two matrices
    matrix1 = g.adjMatrix
    matrix2 = g.adjMatrix

    res = [[0 for x in range(42)] for y in range(42)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
 
                res[i][j] += matrix1[i][k] * matrix2[k][j]
 

    for row in range(0,len(res)):
        for col in range(0,len(res[row])):
            if(res[row][col] != 0 and row != col and row < col):
                print(f'{row},{col},{res[row][col]}')


if __name__ == '__main__':
    reducer()