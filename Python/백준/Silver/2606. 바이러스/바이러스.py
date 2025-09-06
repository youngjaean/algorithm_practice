

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
visted =[False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
def dfs(now_pos):
    global count
    count += 1
    visted[now_pos] =True
    for next_pos in adj[now_pos]:
        if not visted[next_pos]:
            dfs(next_pos)




dfs(1)

print(count - 1)