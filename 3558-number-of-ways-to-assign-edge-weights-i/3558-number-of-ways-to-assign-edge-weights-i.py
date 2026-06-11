class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        max_depth = 0

        def dfs(node, parent, depth):
            nonlocal max_depth

            max_depth = max(max_depth, depth)

            for nxt in graph[node]:
                if nxt != parent:
                    dfs(nxt, node, depth + 1)

        dfs(1, 0, 0)

        return pow(2, max_depth - 1, MOD)