import numpy as np
from numpy.core.defchararray import index
from numpy.lib import index_tricks
from scipy.spatial import distance


def single_linkage(c1, c2):
    """
    Given clusters c1 and c2, calculates the single linkage criterion.
    :param c1: An (N, D) shaped numpy array containing the data points in cluster c1.
    :param c2: An (M, D) shaped numpy array containing the data points in cluster c2.
    :return: A float. The result of the calculation.
    """

    liste = list()
    for i in c1:
        for j in c2:
            temp = (i[0]-j[0])**2 + (i[1]-j[1])**2
            liste.append(np.sqrt(temp))
            
    return min(liste)


def complete_linkage(c1, c2):
    """
    Given clusters c1 and c2, calculates the complete linkage criterion.
    :param c1: An (N, D) shaped numpy array containing the data points in cluster c1.
    :param c2: An (M, D) shaped numpy array containing the data points in cluster c2.
    :return: A float. The result of the calculation.
    """
    liste = list()
    for i in c1:
        for j in c2:

            temp = (i[0]-j[0])**2 + (i[1]-j[1])**2
            liste.append(np.sqrt(temp))
            
    return max(liste)

def average_linkage(c1, c2):
    """
    Given clusters c1 and c2, calculates the average linkage criterion.
    :param c1: An (N, D) shaped numpy array containing the data points in cluster c1.
    :param c2: An (M, D) shaped numpy array containing the data points in cluster c2.
    :return: A float. The result of the calculation.
    """
    calculation = 0
    for i in c1:
        for j in c2:
            temp = (i[0]-j[0])**2 + (i[1]-j[1])**2
            calculation+=np.sqrt(temp)
            
    return calculation/(len(c1)*len(c2))

def centroid_linkage(c1, c2):
    """
    Given clusters c1 and c2, calculates the centroid linkage criterion.
    :param c1: An (N, D) shaped numpy array containing the data points in cluster c1.
    :param c2: An (M, D) shaped numpy array containing the data points in cluster c2.
    :return: A float. The result of the calculation.
    """
    x1 = [0,0] # Variable for storing the sum of the point in c1
    y1 = [0,0] # Variable for storing the sum of the point in c2

    for i in c1: # Add the points 
        x1[0]+=i[0]
        x1[1]+=i[1]
    # Get the averages    
    x1[0] = x1[0]/len(c1)
    x1[1] = x1[1]/len(c1)

    for i in c2:# Add the points 
        y1[0]+=i[0]
        y1[1]+=i[1]
    # Get the averages 
    y1[0] = y1[0]/len(c2)
    y1[1] = y1[1]/len(c2)

    temp = (x1[0]-y1[0])**2 + (x1[1]-y1[1])**2

    return np.sqrt(temp)

def hac(data, criterion, stop_length):
    """
    Applies hierarchical agglomerative clustering algorithm with the given criterion on the data
    until the number of clusters reaches the stop_length.
    :param data: An (N, D) shaped numpy array containing all of the data points.
    :param criterion: A function. It can be single_linkage, complete_linkage, average_linkage, or
    centroid_linkage
    :param stop_length: An integer. The length at which the algorithm stops.
    :return: A list of numpy arrays with length stop_length. Each item in the list is a cluster
    and a (Ni, D) sized numpy array.
    """
    
    clusters = list()
    
    #Since every data is cluster in the beginning at them to the cluster list
    for i in data:
        clusters.append(i.tolist())
   
    while(len(clusters) != stop_length):
        distance = 10000 # Variable for checking the calculated distance is minimum or not

        for i in range(len(clusters)):
            for j in range(len(clusters)):
  
                if((clusters[i]==clusters[j]) or (clusters[i] in clusters[j]) or (clusters[j] in clusters[i])):
                    continue
                else:
                    # Conditions for the shape errors
                    if (np.shape(clusters[i]) != (2,) and np.shape(clusters[j]) != (2,)  ):
                        if(criterion(clusters[i],clusters[j])<distance):
                            distance = criterion(clusters[i],clusters[j])
                            # Get the indexis of the distance
                            cluster1 = i
                            cluster2 = j
                    # Conditions for the shape errors
                    elif (np.shape(clusters[i]) != (2,) and np.shape(clusters[j]) == (2,)  ):
                        if(criterion(clusters[i],[clusters[j]])<distance):
                            distance = criterion(clusters[i],[clusters[j]])
                            # Get the indexis of the distance
                            cluster1 = i
                            cluster2 = j
                    # Conditions for the shape errors
                    elif (np.shape(clusters[i]) == (2,) and np.shape(clusters[j]) != (2,)  ):
                        if(criterion([clusters[i]],clusters[j])<distance):
                            # Get the indexis of the distance
                            distance = criterion([clusters[i]],clusters[j])
                            cluster1 = i
                            cluster2 = j
                    # Conditions for the shape errors
                    else:
                        if(criterion([clusters[i]],[clusters[j]])<distance):
                            # Get the indexis of the distance
                            distance = criterion([clusters[i]],[clusters[j]])
                            cluster1 = i
                            cluster2 = j

        
        # Conditions for the shape errors   
        if (np.shape(clusters[cluster2])!=(2,) and np.shape(clusters[cluster1])==(2,)):
            clusters[cluster2].append(clusters[cluster1])
            clusters.pop(cluster1)
        elif(np.shape(clusters[cluster1])!=(2,) and np.shape(clusters[cluster2])==(2,)):
            clusters[cluster1].append(clusters[cluster2])
            clusters.pop(cluster2)
        elif(np.shape(clusters[cluster1])!=(2,) and np.shape(clusters[cluster2])!=(2,)):
            if len(clusters[cluster1]) > len(clusters[cluster2]):
                # Append the cluster into the big cluster one by one. 
                for item in clusters[cluster2]:
                    clusters[cluster1].append(item)
                clusters.pop(cluster2)
            else:
                for item in clusters[cluster1]:
                    clusters[cluster2].append(item)                
                clusters.pop(cluster1)
        else:
            clusters.append([clusters[cluster1],clusters[cluster2]])    
            clusters.pop(cluster1)
            clusters.pop(cluster2-1)
    
    # The clusters shape is not suitable. Convert the shape of it into suitable shape.
    temp = list()
    for k in range(len(clusters)):
        temp.append(np.vstack(clusters[k]))
    

    return temp





        
    
