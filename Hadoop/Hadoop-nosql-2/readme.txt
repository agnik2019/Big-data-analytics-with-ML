Agnik Saha
Roll : 21CS60A01

Running Instructions
------------------------------------------------
Please write in terminal :

        make run


query1
--------------
group the departments by the number of email communications with other departments and for each group count how many departments belong to the group
Output (stored in result_event.txt)
33 4
39 3
30 2
24 1
38 5
32 3
35 4
....
....
.



query 2
------------------
find all such strongly connected pairs of nodes to create the
event network

Output (stored in result_strong.txt)

0,36
0,4
0,7
1,14
1,15
1,23
1,34
1,36
....
....


query 3
-----------
If there are edges like (v1,v2),
(v2,v3), then the node pair (v1,v2) has one common department

Output (stored in result_common.txt):
0,1,3
0,3,2
0,4,2
0,5,2
0,6,1
0,7,2
0,8,2
0,9,1
0,10,2
0,11,2
.......................



Query 4 
----------------------

Shortest distance from maximum degree vertex to minimum degree vertex
Output

36,33,5 
36,41,3 


