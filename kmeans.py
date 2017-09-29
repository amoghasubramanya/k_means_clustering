# K-means clustering for 100 measurements
import random
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plotsse

#Create a list to store dataset
dataset=[];
#Lists to store 3 clusters
cost=[];

#List of tuples is used to store points.
for i in range(50):
	dataset.append((random.randint(1,50),random.randint(1,50)))
#To sort based on x co-ordinates
px=sorted(dataset)
#To sort based on y co-ordinates
py=sorted(dataset, key=lambda tup: tup[1])


print(dataset)


c1=py[0]
c3=py[24]
c2=py[49]




def distance(x,y):
    """
        Function to caluclate Eucledian Distance
        Calculate euclidean distance
    """
    temp=math.pow((x[0]-y[0]),2)+math.pow((x[1]-y[1]),2)
    dist=math.sqrt(temp)
    return dist


def Clusterassign(p,c1,c2,c3):
    """
    Find out the cluster to which given point belongs to
    """
    if (distance(p,c1) < distance(p,c2)) and (distance(p,c1) < distance(p,c3)):
        return 1 # p belongs to cluster 1
    elif (distance(p,c2) < distance(p,c1)) and (distance(p,c2) < distance(p,c3)):
        return 2 # p belongs to cluster 2
    elif (distance(p,c3) < distance(p,c1)) and (distance(p,c3) < distance(p,c2)):
        return 3 # p belongs to cluster 3



def Centroid(dataset):
    """
    To Calculate Centroid.
    """
    x=0
    y=0
    for i in dataset:
        x=x+i[0]
        y=y+i[1]
    cenx=x/float(len(dataset))
    ceny=y/float(len(dataset))
    return (cenx,ceny)



iterc=1
#To Perform K-Means
def Kmeans(c1,c2,c3,iterc):

    #Step1=We are passing 3 points to the Kmeans algorithm initially, they are chosen as cluster centroids
    centroid1=c1
    centroid2=c2
    centroid3=c3
    label=0
    while True:
        sse=0
        cluster1=[]
        cluster2=[]
        cluster3=[]
       #Step 2: # Assign labels to each datapoint based on centroids
        iterc+=1
        for i in range(50):
            
            label=Clusterassign(dataset[i],centroid1,centroid2,centroid3)
            print(label)
            if label==1:
                cluster1.append(dataset[i])
                sse+=distance(dataset[i],centroid1)**2
            elif label==2:
                cluster2.append(dataset[i])
                sse+=distance(dataset[i],centroid2)**2
            else:
                cluster3.append(dataset[i])
                sse+=distance(dataset[i],centroid3)**2
            
         #Step 3: Assign centroids based on datapoint labels    
        centroid1=Centroid(cluster1)
        centroid2=Centroid(cluster2)
        centroid3=Centroid(cluster3)
         #Convergence check
        if centroid1==c1 and centroid2==c2 and centroid3==c3:
            break
        else:
             #Re-assign centroids with their new means
             c1=centroid1
             c2=centroid2
             c3=centroid3
        sse=sse/50
        cost.append((sse,iterc))
        if (iterc==200):
            break
    print("CLUSTER CENTROIDS ARE:")
    print("\nCLUSTER1:" ,c1[0],' , ',c1[1])
    print("\nCLUSTER2:" ,c2[0],' , ',c2[1])
    print("\nCLUSTER3:" ,c3[0],' , ',c3[1])
    return (cluster1,cluster2,cluster3)


#RUNNING THE ALGORITHM
cluster1,cluster2,cluster3=Kmeans(c1,c2,c3,0)

print(cost)


plotx=[]
ploty=[]


plt.axis([0, 50, 0, 50])
#Displaying cluster1

for i in cluster1:
	plotx.append(i[0])
	ploty.append(i[1])
plt.plot(plotx, ploty, 'bo')


plotx=[]
ploty=[]

#Displaying cluster2

for i in cluster2:
	plotx.append(i[0])
	ploty.append(i[1])
plt.plot(plotx, ploty, 'ro')


plotx=[]
ploty=[]

#Displaying cluster3

for i in cluster3:
	plotx.append(i[0])
	ploty.append(i[1])
plt.plot(plotx, ploty, 'yo')


#Axis Range
plt.axis([0, 50, 0, 50])
#Displaying plot
plt.show()

#Plotting SSE
plt.figure()
plotx=[]
ploty=[]

plotsse.axis([0, len(cost), 0, max(cost[0])])

for i in cost:
    ploty.append(i[0])
    plotx.append(i[1])
plotsse.plot(plotx, ploty, 'b')

plotsse.show()