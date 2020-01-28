import math
import itertools

line_number = 1
max_slices = 0
types = 0
slices = []

with open("d_quite_big.in", "r") as pizza_info:
    for line in pizza_info:
        if line_number == 1:
            numbers = line.split()

            max_slices = int(numbers[0])
            types = int(numbers[1])
            line_number = 2
        else:
            slices = [int(i) for i in line.split()]

print(max_slices)

def average(l):
    return sum(l) / len(l)

subset_size = math.ceil(max_slices / average(slices))
print(subset_size)

final_total = 0
final_subset = []

# r=1812 (quite_big)

def find_r(slices, num):
    largest_subset = 0
    r = 0
    while(largest_subset < num):
        for subset in itertools.combinations(sorted(slices, reverse=True), r=r):
            largest_subset = sum(subset)
            break
            
        r += 10
    
    return r - 10

print(find_r(slices, max_slices))

for subset in itertools.combinations(sorted(slices, reverse=True), r=40):
    #print(sum(subset))
    if sum(subset) > final_total:
        if sum(subset) <= max_slices: 
            final_total = sum(subset)
            final_subset = subset
            if final_total == max_slices:
                break
    else:
        pass#break

print()
print(sum(final_subset))

def subsetsum(array, num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:], (num - array[0])) 
            if with_v is not None:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:], num)

# print(subsetsum(slices, max_slices))

def subsetsum2(array, num):
    if sum(array) >= num:
        return array[:-1]
    if len(array) > 1:
        for subset in (array[:-1], array[1:]):
            result = subsetsum2(subset, num)
            if result is not None:
                return result

# print(subsetsum2(slices, max_slices))

all_sub_sets = []
sub_count = 0

def s(array, num, start_index, target_sum):
    global sub_count
    if target_sum >= num:
        sub_count += 1
        if start_index < len(array):
            s(array, num - array[start_index - 1], start_index, target_sum)
    else:
        for i in range(start_index, len(array)):
            s(array, num + array[i], i + 1, target_sum)

# s(slices, 0, 0, max_slices)
# print(sub_count)

def subsetProb(p_slices, n, sum, sub_set):
    if sum == 0:
        print(sub_set)
        return True
    if n == 0 and sum != 0:
        #print(sub_set)
        return False
    
    if p_slices[n - 1] > sum:
        return subsetProb(p_slices, n-1, sum, sub_set)
    
    return subsetProb(p_slices, n-1, sum, sub_set + [p_slices[n-1]]) or subsetProb(p_slices, n-1, sum-p_slices[n-1], sub_set + [p_slices[n-1]])

# for i in range(10):
#     res = subsetProb(slices, types, max_slices - i, [])
#     print(res, i)

def subsetSum(pizza_set, sub_set, pizza_size, total, nodeCount, sum):
    if total >= sum:
        if total == sum:
            print(sub_set)
        else:
            print(sub_set)
        #sub_set.pop()
        return
    else:
        for i in range(nodeCount, pizza_size):
            subsetSum(pizza_set, sub_set + [pizza_set[i]], pizza_size, total+pizza_set[i], i+1, sum)

def findSubset(pizza_set, size, sum):
    subsetSum(pizza_set, [], size, 0, 0, sum)

#findSubset(slices, types, max_slices)