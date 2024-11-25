from collections import defaultdict

# Using defaultdict with list
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
print(d)  # Output: defaultdict(<class 'list'>, {'a': [1], 'b': [2]})

# Using defaultdict with int
d_int = defaultdict(int)
d_int['a'] += 1
d_int['b'] += 2
print(d_int)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
