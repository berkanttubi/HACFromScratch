Hierarchical Agglomerative Clustering using 4 different criterion. 

The Single Linkage Criterion , The Complete Linkage Criterion, The Average Linkage Criterion,The Centroid Linkage Criterion.

You can see 2 file named hac.py and main.py. Main file controls everything , on the other hand hac file includes the functions needed for HAC algorithms.

### hac.py

+ single_linkage: It takes 2 different clusters, and calculates the Euclidean distance for each item in cluster. It returns the minimum distance value.
+ complete_linkage: It takes 2 different clusters, and calculates the Euclidean distance for each item in cluster. It returns the maximum distance value.
+ average_linkage: It takes 2 different clusters, and calculates the Euclidean distance for each item in cluster. Add them up ,dive it to the (M*N) and returns the value.
+ centroid_linkage: It takes 2 different clusters, x1 variable is for first cluster, y1 variable is for second cluster. It adds up to x and y values of both clusters to the  x1 and y1 variables. Then gets the averages differently, calculates the distance from those averages and returns them.
+ hac: Initially, it adds every data point to the "clusters" variable since they are cluster of their own. Then while length of this "clusters" varibale equals to the stop_length the loop works. For example if stop_length = 3; length of "clusters" is 3 also , since there are 3 different clusters at the end.  "Distance" variable is just for comparison for minimum distance value, and its default value is chose nrandomly. Since we are getting the min value it does not affect the algorithm. In loops, the algorithm basically calculates the every distance based on the given function in the input parameter called "criterion" among the all clusters. Then stores the minimum distance and its indexes. The purpose of if's in the loop is that preventing the error caused from shape.When the min distance and indexes are figured out, they will cluster with each other and their previous values removed from the list, since they are new cluster now. The if values after the loops is just for again preventing from the shape error problems. If any 2 cluster that has more than 1 example inside it, The algorithm compare them and appends the small cluster into big cluster. Whenever the cluster length reaches to the stop_length , it means we are done. After clustering part is done, there is a loop again. It is just for the shape purposes again. 		

### main.py

​	criterions and k_values are given manually. For every dataset, the program tries every linkage method differently and plot them. 