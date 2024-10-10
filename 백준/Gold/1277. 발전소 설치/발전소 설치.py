import heapq
import math

n,w=map(int,input().split())
m=float(input())
plants=dict()

for i in range(1,n+1):
    x,y=map(int,input().split())
    plants[i]=(x,y)

INF=1e9
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
existed=set()

for _ in range(w):
    start,end=map(int,input().split())
    existed.add((start,end))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            if (i,j) not in existed and (j,i) not in existed:
                dist=math.sqrt((plants[i][0]-plants[j][0])**2+(plants[i][1]-plants[j][1])**2)
                if dist<=m:
                    graph[i].append((j,dist))
            else:
                graph[i].append((j,0))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
print(int(distance[n]*1000))