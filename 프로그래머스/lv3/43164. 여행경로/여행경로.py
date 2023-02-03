import collections

def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop(0))
        answer.append(airport)

    dfs('ICN')
    return answer[::-1]