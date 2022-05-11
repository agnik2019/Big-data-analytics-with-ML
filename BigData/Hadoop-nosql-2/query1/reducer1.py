# Name:reducer1.py

import  sys

my_dict = {} # dictionary of list

# initialization of dictionary
for i in range(0,42):
    my_dict[i] = list()

#Function to calculate chat counts
def reducer():
    current_node=""
    current_count=0
    node=""
    for line in sys.stdin:
        line=line.strip()
        #splitting string with "#" separated nodes
        l_arr=line.split("#")
        nodes_arr=l_arr[0]
        nodes=nodes_arr.split(",")
        node0 = nodes[0]
        node1 = nodes[1]
        # print(f"{node0} and {node1}")
        if int(node1) not in my_dict[int(node0)]:
            my_dict[int(node0)].append(int(node1))

        if int(node0) not in my_dict[int(node1)]:
            my_dict[int(node1)].append(int(node0))

    #print(my_dict)
    len_dict = {}

    for key in my_dict:
       # print(f'{key} {len(my_dict[key])}') 
       len_dict[key] = len(my_dict[key])
    
    # print(len_dict)

    res = {}
    for i,v in len_dict.items():
        
        res[v] = [i] if v not in res.keys() else res[v]+[i]

    # print(res)

    for key in res:
        if key != 0:
             print(f'{key} {len(res[key])}') 


       

if __name__ == "__main__":
    reducer()