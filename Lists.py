
EMPTY = 0
Capacity = 10
MAX_ITEMS = 6
# knapsack = [[EMPTY for i in range(MAX_ITEMS)] for k in range(Capacity)]
def init_knapsack(items, capacity):
    global knapsack
    knapsack = [[EMPTY for i in range(items + 1)] for k in range(capacity + 1)]


def O(K,j,items):
    k = K
    if k == 0 or j == 0:
        return knapsack[0][0]

    v,w = items[j]
    if w > k: knapsack[K][j] = knapsack[K][j-1]

    while w <= k:
        if v + knapsack[k-w][j-1] > knapsack[k][j-1]:
            knapsack[k][j] = v + knapsack[k-w][j-1]
            k = k - w
        else:
            knapsack[k][j] = knapsack[k][j-1]
            k = k - items[j-1][1]
    return knapsack[K][j]


def print_ks():
    for k in knapsack:
        print(k)

# Soln set for k = 9 and j = 3
def solve(capacity, items):
    item_cnt = len(items)
    init_knapsack(item_cnt, capacity)
    for i in range(item_cnt):
        for k in range(1,capacity+1):
            O(k,i,items)
    print_ks()
    k = capacity
    j = item_cnt - 1
    soln_list = [0 for i in range(j)]
    print(soln_list)
    
    while k > 0 and j > 0:
        if knapsack[k][j] != knapsack[k][j-1]:
            soln_list[j-1] = 1
            k = k - items[j][1]
        else:
            soln_list[j-1] = 0
        j = j-1
    return soln_list


# list of (value, weight) tuples 
item_list = [
    [(0,0),(5,4),(6,5),(3,2)],
    [(0,0),(16,2),(19,3),(23,4),(28,5)]
]    

soln = solve(7,item_list[1])
print("Soln is ",soln)
    

