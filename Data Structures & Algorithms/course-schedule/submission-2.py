class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = {}
        adj = collections.defaultdict(list)

        for a,b in prerequisites:
            adj[b].append(a)
            state[b] = state.get(b,0)

        for i in range(numCourses):
            if i not in state:
                state[i] = 0
        

        
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course]==2:
                return True
            state[course] = 1
            for i in adj[course]:
                if not dfs(i):
                    return False
            state[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
    
        return True
            
        