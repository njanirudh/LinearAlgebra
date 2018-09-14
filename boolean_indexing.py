import numpy as np

names = np.array(['ali','bob','chad','daisy'])
scores = np.array([
    [40,45,42],
    [10,15,7],
    [50,50,49],
    [50,2,50]
])

print(names == 'bob',"\n")
print(scores[names == 'bob'],"\n")

# Set all values of the row to 100
scores[names == 'bob'] = 100
print(scores,"\n")
