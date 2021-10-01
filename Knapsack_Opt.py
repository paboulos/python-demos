import time 
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

EMPTY = 0

# Adds extra first column for zeroes
def init_knapsack(item_cnt, capacity):
    global knapsack
    knapsack = [[EMPTY for i in range(item_cnt+1)] for k in range(capacity + 1)]

# Update Column j for Capacity K
def O(K,j,items):
    k = K
    if k == 0 or j == 0:
        return knapsack[0][0]

    _,value,weight = items[j-1]
    if weight > k: knapsack[K][j] = knapsack[K][j-1]

    while weight <= k:
        if value + knapsack[k-weight][j-1] > knapsack[k][j-1]:
            knapsack[k][j] = value + knapsack[k-weight][j-1]
            k = k - weight
        else:
            knapsack[k][j] = knapsack[k][j-1]
            k = k - items[j-2].weight
    return knapsack[K][j]


def print_ks():
    for k in knapsack:
        print(k)

# Soln 
def solve(capacity, items):
    item_cnt = len(items)
    init_knapsack(item_cnt, capacity)
    for i in range(item_cnt+1):
        for k in range(1,capacity+1):
            O(k,i,items)
    #print_ks()
    k = capacity
    j = item_cnt
    soln_list = [0 for i in range(j)]
    # Trace Back Knapsack Grid
    while k > 0 and j > 0:
        if knapsack[k][j] != knapsack[k][j-1]:
            soln_list[j-1] = 1
            k = k - items[j-1].weight
        else:
            soln_list[j-1] = 0
        j = j-1
    return soln_list


# list of (value, weight) tuples 
item_list = [
            [Item(index=0,value=5, weight=4),
             Item(index=1,value=6,weight=5),
             Item(index=2,value=3, weight=2)],
            [Item(index=0,value=16,weight=2),
             Item(index=1,value=19,weight=3),
             Item(index=2,value=23,weight=4),
             Item(index=3,value=28,weight=5)],
            [Item(index=0,value=8,weight=4),
             Item(index=1,value=10,weight=5),
             Item(index=2,value=15,weight=8),
             Item(index=3,value=4,weight=3)]]

big_list = [(90001,90000),(89751,89750),(10002,10001),(89501,89500),(10254,10252),
            (89251,89250),(10506,10503),(89001,89000),(10758,10754),(88751,88750),
            (11010,11005),(88501,88500),(11262,11256),(88251,88250),(11514,11507),
            (88001,88000),(11766,11758),(87751,87750),(12018,12009),(87501,87500),
            (12270,12260),(87251,87250),(12522,12511),(87001,87000),(12774,12762),
            (86751,86750),(13026,13013),(86501,86500),(13278,13264),(86251,86250),
            (13530,13515),(86001,86000),(13782,13766),(85751,85750),(14034,14017),
            (85501,85500),(14286,14268),(85251,85250),(14538,14519),(86131,86130)
            ]
big_item_list = [Item(index=0, value=90001, weight=90000), Item(index=1, value=89751, weight=89750), Item(index=2, value=10002, weight=10001), Item(index=3, value=89501, weight=89500), Item(index=4, value=10254, weight=10252), Item(index=5, value=89251, weight=89250), Item(index=6, value=10506, weight=10503), Item(index=7, value=89001, weight=89000), Item(index=8, value=10758, weight=10754), Item(index=9, value=88751, weight=88750), Item(index=10, value=11010, weight=11005), Item(index=11, value=88501, weight=88500), Item(index=12, value=11262, weight=11256), Item(index=13, value=88251, weight=88250), Item(index=14, value=11514, weight=11507), Item(index=15, value=88001, weight=88000), Item(index=16, value=11766, weight=11758), Item(index=17, value=87751, weight=87750), Item(index=18, value=12018, weight=12009), Item(index=19, value=87501, weight=87500), Item(index=20, value=12270, weight=12260), Item(index=21, value=87251, weight=87250), Item(index=22, value=12522, weight=12511), Item(index=23, value=87001, weight=87000), Item(index=24, value=12774, weight=12762), Item(index=25, value=86751, weight=86750), Item(index=26, value=13026, weight=13013), Item(index=27, value=86501, weight=86500), Item(index=28, value=13278, weight=13264), Item(index=29, value=86251, weight=86250), Item(index=30, value=13530, weight=13515), Item(index=31, value=86001, weight=86000), Item(index=32, value=13782, 
weight=13766), Item(index=33, value=85751, weight=85750), Item(index=34, value=14034, weight=14017), Item(index=35, value=85501, weight=85500), Item(index=36, value=14286, weight=14268), Item(index=37, value=85251, weight=85250), Item(index=38, value=14538, weight=14519), Item(index=39, value=86131, weight=86130)]

# duplicate or find and delete from list 
# g = (x for x, e in enumerate(items) if e.index == i)
# items.pop(next(g))
# dup_items = big_item_list[:]

# Convert items to indexed dictionary of items
def item_to_dict(src_list):
   dic={}
   for i in src_list:
      dic[i.index]=i
   return dic

# Remove used items from dictionary
def remove_items(used_items, remaining_items, item_dict):
    for i in range(len(used_items)):
        if used_items[i] == 1:
            index = remaining_items[i].index
            del item_dict[index]

def update_full_soln(new_soln, soln, items):
    for i in range(len(new_soln)):
        if new_soln[i] == 1:
            index = items[i].index
            soln[index] = 1
            
def soln_value(soln, items):
    val = 0
    for i in range(len(soln)):
        if soln[i] == 1:
            val += items[i].value
    return val
            
def sub_opt_soln(K, max_k, item_dict):
    full_soln = [0 for i in range(len(item_dict.keys()))]
    final_val = 0
    #print("Testing Items: ",test_items)
    while K > 0:
        # dict vals to list
        test_items = list(item_dict.values())
        if K > max_k:
            soln = solve(max_k, test_items)
            #print("Partial Value:",knapsack[max_k][len(test_items)])
            final_val += knapsack[max_k][len(test_items)]
            update_full_soln(soln, full_soln, test_items)
            remove_items(soln, test_items, item_dict)
            K -= max_k
        else:
            soln = solve(K, test_items)
            #print("Partial Value:",knapsack[K][len(test_items)])
            final_val += knapsack[K][len(test_items)]
            update_full_soln(soln, full_soln, test_items)
            K -= K
    return (final_val,full_soln)
start = time.time()
K=100000
max_k = 50000

item_dict = item_to_dict(big_item_list)
final_val, final_soln = sub_opt_soln(K, K, item_dict)
print("Final Value: ", final_val)
print("Final Soln: ", final_soln)
finish = time.time()
print("Timer/sec: ",finish-start)

outputData = str(final_val)+ ' '+str(0)+'\n'
outputData += ' '.join(map(str,final_soln))
print("K=%d Solution: "%(K))
print(outputData)

    

