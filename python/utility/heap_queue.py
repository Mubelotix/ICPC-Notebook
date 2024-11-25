import heapq

# Create an empty priority queue (heap)
pq = []

# Insert elements into the priority queue
heapq.heappush(pq, 15)
heapq.heappush(pq, 31)
heapq.heappush(pq, 3)
heapq.heappush(pq, 482)

# Pop the smallest element
print(heapq.heappop(pq))  # Output: 3

# The next smallest element
print(heapq.heappop(pq))  # Output: 15
