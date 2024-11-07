#User function Template for python3

def dfs(value,adj,visited,result):
    visited[value]=1
    result.append(value)
    for i in adj[value]:

        if(visited[i]!=1):
            result=dfs(i,adj,visited,result)
    return result

class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        result=[]
        visited=[0]*len(adj)
        
        dfs(0,adj,visited,result)
    
            
        return result
        
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        print("~")
        T -= 1

# } Driver Code Ends