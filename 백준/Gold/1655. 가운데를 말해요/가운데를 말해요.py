import heapq
import sys
n = int(sys.stdin.readline())
left_heap = []
right_heap = []
result = []

for _ in range(n):
    elem = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-elem, elem))
    else:
        heapq.heappush(right_heap, (elem, elem))

    if right_heap and left_heap[0][1] > right_heap[0][0]:
        min = heapq.heappop(right_heap)[0]
        max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min, min))
        heapq.heappush(right_heap, (max, max))
    result.append(left_heap[0][1])

for i in result:
    print(i)