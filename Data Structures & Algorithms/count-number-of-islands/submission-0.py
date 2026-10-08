class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #edge case
        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        output = 0 #num of islands counted

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while queue: #check surroundings of island
                (coords_r , coords_c) = queue.popleft()

                for dr,dc in directions:
                    exp_r = coords_r + dr
                    exp_c = coords_c + dc

                    if ((exp_r in range(rows)) and (exp_c in range(columns)) and (grid[exp_r][exp_c] == "1") and (exp_r,exp_c) not in visited):
                        queue.append((exp_r,exp_c))
                        visited.add((exp_r,exp_c))


        for r in range(rows):
            for c in range(columns):
                #if grid is island, start BFS to search for more islands
                if (grid[r][c] == "1" and (r,c) not in visited):
                    bfs(r,c)
                    output += 1
        
        return output

