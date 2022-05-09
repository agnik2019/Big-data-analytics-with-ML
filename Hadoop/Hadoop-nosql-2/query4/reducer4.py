
import  sys

my_dict = {} # dictionary of list

# initialization of dictionary
for i in range(0,42):
    my_dict[i] = list()

# initialization of graph
class Graph(object):

    def __init__(self, vertices):
        self.adjMatrix = []
        for i in range(vertices):
            self.adjMatrix.append([0 for i in range(vertices)])
        self.vertices = vertices

        # Add edges
    def add_edge(self, v1, v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt


     
    def minDistance(self, dist, sptSet):
 
        min = 1e7
 
        for v in range(42):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self, src):
 
        dist = [1e7] * 42
        dist[src] = 0
        sptSet = [False] * 42
 
        for cout in range(42):
 
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True
 
            for v in range(42):
                if (self.adjMatrix[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.adjMatrix[u][v]):
                    dist[v] = dist[u] + self.adjMatrix[u][v]
 
        #self.printSolution(dist)
        return dist



# THis function returns degree of a particular node          
def findDegree(G, ver):
    degree = 0
    for i in range(42):
        if G[ver][i] >= 1:
            degree += 1
    if G[ver][ver] >= 1: 
        degree += 1
    return degree    


my_list = []
def reducer():
    g = Graph(42)
    # creating dictionary with all nodes that has an email communication with a particular node
    for line in sys.stdin:
        line=line.strip()
        nodes=line.split(",")
        node0 = nodes[0]
        node1 = nodes[1]

        temp = node0+","+node1
        my_list.append(temp)

        my_dict[int(node0)].append(int(node1))
        my_dict[int(node1)].append(int(node0))

    for line in my_list:
        line=line.strip()
        nodes=line.split(",")
        node0 = nodes[0]
        node1 = nodes[1]
        wt = my_dict[int(node0)].count(int(node1)) # number of email communication that exists between the two departments
        g.add_edge(int(node0),int(node1),wt)


    degree_map = {}
    for i in range(42):
        degree_map[i] = findDegree(g.adjMatrix,i)
    
    #print(degree_map)
    max_degree = max(degree_map, key= lambda x: degree_map[x])
    #print(max_degree)

    minimum_value = min(degree_map.values())
    #print(minimum_value)
    min_degrees = [key for key in degree_map if degree_map[key]==minimum_value]

    #print(min_degrees)

    # MAx_degree with node 36
    # Min degree with node 33 and 41
    # We need to find shortest path from node 36 to 33
    # we need to shortest distance path from 36 to 41

    # implementing dijkstra's algorithm

    dist = g.dijkstra(max_degree)

    for mind in min_degrees:
        print(f"{max_degree},{mind},{dist[mind]} ")

       

if __name__ == "__main__":
    reducer()