import math
import itertools
import time

file_name = "b_small"
line_number = 1
max_slices = 0
types = 0
slices = []

with open(file_name + ".in", "r") as pizza_info:
    for line in pizza_info:
        if line_number == 1:
            numbers = line.split()
            max_slices = int(numbers[0])
            types = int(numbers[1])
            line_number = 2
        else:
            slices = [int(i) for i in line.split()]

print(max_slices, types, slices)

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
    return r

def find_s(r):
    final_total = 0
    final_subset = []

    current_time = time.time()

    for subset in itertools.combinations(sorted(slices, reverse=True), r=r):

        if ((time.time() - current_time) > 5):
            return None
        
        print(subset)
        print(sum(subset))
        if sum(subset) > final_total:
            if sum(subset) <= max_slices: 
                final_total = sum(subset)
                final_subset = subset
                if final_total == max_slices:
                    break
        else:
            pass

    if final_subset == []:
        return None

    return final_subset

r_val = find_r(slices, max_slices)
current_guess = []
for i in range(r_val, r_val-11, -1):
    res = find_s(i)
    if res is None:
        continue
    if sum(res) != max_slices:
        current_guess = res
        continue

    current_guess = res
    break

indexes = []
index_counter = 0

for index in range(len(slices) - 1, 0, -1):
    if index_counter == len(current_guess):
        break

    pizza_slice = slices[index]
    guess_val = current_guess[index_counter]
    if guess_val == pizza_slice:
        index_counter += 1
        indexes.append(index)

indexes = sorted(indexes)

print(indexes)
print(current_guess)
print(sum(current_guess))

out = ""
for i in indexes:
    out = out + str(i) + " "
out = out[:-1]
with open(file_name + ".out", "w") as pizza_out:
    pizza_out.write(str(len(indexes)) + "\n")
    pizza_out.write(out)
