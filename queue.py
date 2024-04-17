from collections import deque 
queue = deque()
queue.append('Susan')
queue.append('Mwende')
queue.append('Masaku')
queue.append('Patricia')
print(queue)

print(queue.popleft())
print(queue.pop())

