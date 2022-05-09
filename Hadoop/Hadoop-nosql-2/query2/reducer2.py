# Name:reducer1.py
# Agnik Saha(21CS60A01)

import  sys

def reducer():
    current_node=""
    current_count=0
    node=""
    for line in sys.stdin:
        line=line.strip()
        #splitting string with "$" separated nodes
        l_arr=line.split("#")
        node=l_arr[0]

        try:
            count=int(l_arr[1])
        except ValueError:
            continue

        #update current count 
        if (current_node=="" or node==current_node):
            current_count+=count
        else:
            #update count  and output if count >= 50
            if (current_count >= 50 and current_node):
                print(current_node)
            current_count=count
        current_node=node

    #output the last node if needed!
    if current_node == node:
        if(current_count >= 50 and current_node):
            print(current_node)

if __name__ == "__main__":
    reducer()