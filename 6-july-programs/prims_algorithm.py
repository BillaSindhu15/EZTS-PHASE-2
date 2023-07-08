import heapq
def prims(graph,start):
    parents={}
    weights={}
    queue=[]
    visited=set()
    for vertex in graph:
        weights[vertex]=99999
    weights[start]=0
    heapq.heappush(queue,(0,start))
    #print(queue)
    while len(queue)!=0:
        curr_weight,curr_node=heapq.heappop(queue)
        if curr_node in visited:
            continue
        for weight,node in graph[curr_node]:
            #print(weight,node)
            if node not in visited and weight < weights[node]:
                weights[node]=weight
                parents[node]=curr_node
                heapq.heappush(queue,(weight,node))
            visited.add(curr_node)
    print(weights)
    print(parents)
                
                
graph={
    'A':[(10,'F'),(28,'B')],
    'B':[(28,'A'),(14,'G'),(16,'C')],
    'C':[(16,'B'),(12,'D')],
    'D':[(12,'C'),(18,'G'),(22,'E')],
    'E':[(25,'F'),(24,'G'),(22,'D')],
    'F':[(10,'A'),(25,'E')],
    'G':[(14,'B'),(18,'D'),(24,'E')]
    }
mst=prims(graph,'A')