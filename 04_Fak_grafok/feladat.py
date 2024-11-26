#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

import heapq

def getCost(g_nodes, g_from, g_to, g_weight):
    MOD = 10**9 + 7
    graph = [[] for _ in range(g_nodes + 1)]
    
    for u, v, w in zip(g_from, g_to, g_weight):
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    pq = [(0, 1)]
    min_cost = [float('inf')] * (g_nodes + 1)
    min_cost[1] = 0
    
    while pq:
        current_cost, u = heapq.heappop(pq)
        
        if current_cost > min_cost[u]:
            continue
        
        for v, weight in graph[u]:
            cost_to_v = max(weight, current_cost)
            if cost_to_v < min_cost[v]:
                min_cost[v] = cost_to_v
                heapq.heappush(pq, (cost_to_v, v))
    
    result = min_cost[g_nodes]
    
    if result == float('inf'):
        print("NO PATH EXISTS")
    else:
        print(result)

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)