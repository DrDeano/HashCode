line_number = 1
max_slices = 0
types = 0
slices = []

with open("b_small.in", "r") as pizza_info:
    for line in pizza_info:
        if line_number == 1:
            numbers = line.split()

            max_slices = int(numbers[0])
            types = int(numbers[1])
            line_number = 2
        else:
            slices = [int(i) for i in line.split()]

total_slices = 0
indexes = []
for i in range(len(slices)-1, -1, -1):
    if (slices[i] + total_slices < max_slices):
        total_slices += slices[i]
        indexes.append(i)

indexes.sort()


print(max_slices, types, slices)
print(total_slices, indexes)