import heapq

def solution(k, score):
    answer = []
    heap = []
    for num in score:
        if len(heap) < k:
            heapq.heappush(heap, num)
            answer.append(heap[0])
            continue
        if len(heap) == k and heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        answer.append(heap[0])
        
    return answer