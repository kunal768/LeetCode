class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = collections.defaultdict(lambda : [])
        for path in paths:
            g[path[0]].append(path[1])
            g[path[1]].append(path[0])
        plants = [0]*N
        for node in g :
            colors = { 1, 2, 3, 4 }
            for adj in g[node]:
                if plants[adj-1] != 0 and plants[adj-1] in colors :
                    colors.remove(plants[adj-1])
            plants[node-1] = colors.pop()
        
        for i in range(N):
            if plants[i] == 0 :
                plants[i] = 1
        return plants