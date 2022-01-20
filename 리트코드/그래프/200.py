from collections import deque
def bfs(start, grid):
    y,x = start
    dy = [ 0 , 1, -1 ,0]
    dx = [-1,0,0,1]
    queue = deque([[y,x]])
    visited = [[y,x]]
    while queue:
        cury, curx = queue.popleft()
        grid[cury][curx] ='2'
        for i in range(4):
            nexty, nextx = dy[i] + cury, dx[i] +curx
            if [nexty, nextx] not in visited and 0 <= nexty <len(grid) and 0 <= nextx< len(grid[0]) and grid[nexty][nextx] == '1' :
                visited.append([nexty, nextx])
                queue.append([nexty, nextx])
    return grid

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    count += 1
                    grid = bfs([y,x], grid)
        return count