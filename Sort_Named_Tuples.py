from collections import namedtuple
"""
Explicit Types with named tuples assign meaningful names to the positions of the tuple’s elements.
A named tuple is a subclass of tuple. It also adds property names to the positional elements.
"""
Item = namedtuple("Item",['index','value','weight'])

def collect_items(n, items:Item):
    list = []
    for i in range(n):
        _,value,weight = items[i]
        list.append((value,weight))
    return list

lines = ["","1 8","2 4","3 5"]
item_count = 3
items = []
sum_w = 0
sum_v = 0

for i in range(1, item_count+1):
    line = lines[i]
    parts = line.split()
    sum_v += int(parts[0])
    sum_w += int(parts[1])
    items.append(Item(i-1, int(parts[0]), int(parts[1])))

avg_w = sum_w/item_count
avg_v = sum_v/item_count
print("Avg value and weight = ",avg_v,avg_w)
my_items = collect_items(item_count, items)
print("item Type is ",type(items[0]))
print(Item(4,1,8) in items)
items.remove(Item(0,1,8))
print(items)
#list Sort in-place ascending
#items.sort(key=lambda item: item.value/item.weight,reverse=True)
sort_lst = sorted(items,key=lambda item: item.value/item.weight,reverse=True)
print("Sorted list")
print(sort_lst)
print(my_items)
