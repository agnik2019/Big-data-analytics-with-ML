# Agnik Saha
# Roll 21CS60A01
import  sys
 
def take_single_xy_yx(x):
    # (X,Y) AND (Y,X) both nodes are not accepted so I consider them as single node
   if(int(x[0]) > int(x[1])):
       node = x[1] + "," + x[0]
   else:
       node = x[0] + "," + x[1]
   return node
 
def combiner():
   current_node=""
   current_count=0
   for line in sys.stdin: 
       # remove spaces from lines
       line=line.strip()
       try:
           temp = line.split(";")
           nodes = temp[0]
           x = nodes.split(",")
       except:
           continue
      
       try:
           node = take_single_xy_yx(x)
           count = int(temp[1])
       except ValueError:
           continue
 
       if (current_node=="" or node==current_node):
           current_count+=count
       else:
           # format : node0, node1 # count
           print(current_node+"#"+str(current_count))
           current_count=count
       current_node=node
 
   try:
       # consider last node
       if current_node == node:
           print(current_node+"#"+str(current_count))
   except:
       pass
 
if __name__ == "__main__":
   combiner()