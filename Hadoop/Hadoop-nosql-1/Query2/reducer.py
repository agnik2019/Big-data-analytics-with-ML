# Agnik Saha
# Roll: 21CS60A01
# Query 2
# Selection sort is used here

import  sys
current_node=""
current_count=0
no_of_employee=["0,0","0,0","0,0","0,0","0,0","0,0","0,0","0,0","0,0","0,0"] #"current_node, current_count"

# reading line by stdin
for line in sys.stdin:
    line=line.strip()
    temp=line.split(",")
    node=temp[0]
    try:
        count=int(temp[1])
        # count 
    except ValueError:
        continue

    if(current_node=="" or node==current_node):
        current_count+=count
    else:
        # I am using selection sort here
        main_arr = list(no_of_employee[9].split(","))
        if(current_count>int(main_arr[1])):
            no_of_employee[9]=str(current_node) + "," + str(current_count)
            for i in range(8,-1,-1):
                # Implementing insertion sort previous elements
                arr = list(no_of_employee[i].split(",")) #"current_node, current_count"
                if(int(arr[1]) < current_count):
                    temp_node=int(arr[0])  # node
                    temp_count=int(arr[1])  # count
                    no_of_employee[i]=no_of_employee[i+1] # selection
                    no_of_employee[i+1]= str(temp_node) + "," + str(temp_count)

        current_count=count
    current_node=node
#output the last node if needed!
if current_node == node:
    main_arr = list(no_of_employee[9].split(","))
    if(current_count>int(main_arr[1])):
        no_of_employee[9]=str(current_node) + "," + str(current_count)
        for i in range(8,-1,-1):
            arr = list(no_of_employee[i].split(","))
            if(int(arr[1]) < current_count):
                temp_node=int(arr[0])
                temp_count=int(arr[1])
                no_of_employee[i]=no_of_employee[i+1]
                no_of_employee[i+1]= str(temp_node) + "," + str(temp_count)

for no in range(0,10):
    main_arr = list(no_of_employee[no].split(","))
    print(main_arr[0]) # storing top 10 employees


