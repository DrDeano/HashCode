import math
import itertools
import signal
import time

line_number = 1
max_slices = 0
types = 0
slices = []

with open("a_example.in", "r") as pizza_info:
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

# r=1812 (quite_big)

def find_r(slices, num):
    largest_subset = 0
    r = 0


    while(largest_subset < num):
        if len(slices) < 10 + r:
            r = len(slices)
        else:
            r += 10

        for subset in itertools.combinations(sorted(slices, reverse=True), r=r):
            largest_subset = sum(subset)
            break
        
        # if len(slices) < 10 + r:
        #     r = len(slices)
        # else:
        #     r += 10
    
    return r

print(find_r(slices, max_slices))

def find_s(r):
    final_total = 0
    final_subset = []

    current_time = time.time()

    for subset in itertools.combinations(sorted(slices, reverse=True), r=r):
        if time.time() - current_time > 2:
            print("blah")
            return None
        
        #print(sum(subset))
        if sum(subset) > final_total:
            if sum(subset) <= max_slices: 
                final_total = sum(subset)
                final_subset = subset
                if final_total == max_slices:
                    break
        else:
            pass#break
    
    return final_subset

r_val = find_r(slices, max_slices)

for i in range(r_val, r_val-10, -1):
    print(i)
    res = find_s(i)
    if res is None:
        continue

    print()
    print(sum(res))
    break
