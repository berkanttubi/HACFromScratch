import numpy as np
from hac import single_linkage, complete_linkage, average_linkage, centroid_linkage, hac
import matplotlib.pyplot as plt

def plot_clusters(data,j):
    colors = ["red","blue","green","black"]
    criterion = ["single_linkage","complete_linkage","average_linkage","centroid_linkage"]
    counter= 0
    plt.title(criterion[j])
    for i in data:
        x = [ j[0] for j in i]
        y = [ j[1] for j in i]
        plt.scatter(x,y,color = colors[counter])
        counter+=1

    plt.show()
if __name__ == '__main__':
    dataset = list()
    dataset.append(np.load('dataset1.npy'))
    dataset.append(np.load('dataset2.npy'))
    dataset.append(np.load('dataset3.npy'))
    dataset.append(np.load('dataset4.npy'))
    criterion = [single_linkage,complete_linkage,average_linkage,centroid_linkage]
    k_values = [2,2,2,4]

    for i in range(len(dataset)):
        for j in range(len(criterion)):
            result = hac(dataset[i], criterion[j], k_values[i])
            plot_clusters(result,j)
    

    

    