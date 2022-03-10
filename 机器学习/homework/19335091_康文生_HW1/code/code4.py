import numpy as np
import pandas as pd
import math
import random

def dfs(grid,r,c):
    grid[r][c] += 1
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return True
    dire = [-1,0,1,0,-1]
    dir_list = []

    for i in range(4):
        x,y = r + dire[i],c + dire[i+1]
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            continue
        if x == 3 and y == 3:
            if grid[x][y] == 2:
                continue
        else :
            if grid[x][y] == 1:
                continue
        dir_list.append([x,y])

    if len(dir_list) == 0:
        return False
    ra = random.randint(0,len(dir_list) - 1)
    return dfs(grid,dir_list[ra][0],dir_list[ra][1])


import copy
if __name__ == "__main__":
    ret = 0
    row = []
    for j in range(7):
        row.append(0)
    grid = []
    for j in range(7):
        grid.append(row[0:])
    for i in range(20000):
        if dfs(copy.deepcopy(grid),0,0) == True:
            ret += 1

    print(ret)
    p = ret/20000
    print(p)
