#User function Template for python3
from collections import deque
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj):
        #code here
        
        result=[]
        visited=[0]*len(adj)
        q=deque([])
        q.append(0)
        while(len(q)>0):
            x=q.popleft()
            visited[x]=1
            result.append(x)
            
            for h in adj[x]:
                if visited[h]!=1:
                    q.append(h)
                    visited[h]=1
                
    
                    
        
        return result
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # This line ensures the graph is undirected
        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        print("~")

# } Driver Code Ends