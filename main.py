import math
from timeit import default_timer as timer

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]



with open('KnapsackValues.txt') as f:
    val = f.readlines()
    val = list(map(int, val))

with open('KnapsackWeights.txt') as f:
    wt = f.readlines()
    wt = list(map(int, wt))

# Driver program to test above function
W = 5000
n = len(val)
print(knapSack(W, wt, val, n))

trials = 100
for i in range (0,trials):
    begin = timer()
    knapSack(W, wt, val, n)
    end = timer()
    executionTime = (end - begin)*1000000
    print(executionTime)

# This code is contributed by Bhavya Jain