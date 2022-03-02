from collections import Counter
s = 'abc'

counts= Counter()
counts[s[1]] += 1
print(counts)