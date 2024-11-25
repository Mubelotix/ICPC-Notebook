from bisect import bisect_left, bisect_right, insort

data = [10, 20, 30, 40]  # Must be sorted
insort(data, 25)  # Insert 25 into the correct position
print(data)  # Output: [10, 20, 25, 30, 40]

# Find the position to insert 35 while maintaining order
pos = bisect_left(data, 35)
print(pos)  # Output: 4 (index where 35 should be inserted)

# Find the range of elements between 20 and 35
start = bisect_left(data, 20)
end = bisect_right(data, 35)
print(data[start:end])  # Output: [20, 25, 30]
