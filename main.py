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

total_slices = 0
indexes = []
for i in range(len(slices)-1, -1, -1):
    if (slices[i] + total_slices < max_slices):
        total_slices += slices[i]
        indexes.append(i)

indexes.sort()


print(max_slices, types, slices)
print(total_slices, indexes)


# void subsetSum(int set[], int subSet[], int n, int subSize, int total, int nodeCount ,int sum) {
#    if( total == sum) {
#       displaySubset(subSet, subSize);     //print the subset
#       subsetSum(set,subSet,n,subSize-1,total-set[nodeCount],nodeCount+1,sum);     //for other subsets
#       return;
#    }else {
#       for( int i = nodeCount; i < n; i++ ) {     //find node along breadth
#          subSet[subSize] = set[i];
#          subsetSum(set,subSet,n,subSize+1,total+set[i],i+1,sum);     //do for next node in depth
#       }
#    }
# }

# void findSubset(int set[], int size, int sum) {
#    int *subSet = new int[size];     //create subset array to pass parameter of subsetSum
#    subsetSum(set, subSet, size, 0, 0, 0, sum);
#    delete[] subSet;
# }

def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

print(subsetsum(slices, max_slices))


def subsetProb(p_slices, n, sum, sub_set):
    if sum <= 0:
        print(sub_set)
        return True
    if n == 0 and sum != 0:
        return False
    
    if p_slices[n - 1] > sum:
        return subsetProb(p_slices, n-1, sum, sub_set)
    
    sub_set.append(p_slices[n-1])
    return subsetProb(p_slices, n-1, sum, sub_set) or subsetProb(p_slices, n-1, sum-p_slices[n-1], sub_set)

# subsetProb(slices, types, max_slices, [])

def subsetSum(pizza_set, sub_set, pizza_size, total, nodeCount, sum):
    if total >= sum:
        if total == sum:
            print(sub_set)
        else:
            print(sub_set)
        return
    else:
        for i in range(nodeCount, pizza_size):
            sub_set.append(pizza_set[i])
            subsetSum(pizza_set, sub_set, pizza_size, total+pizza_set[i], i+1, sum)

def findSubset(pizza_set, size, sum):
    subsetSum(pizza_set, [], size, 0, 0, sum)


# findSubset(slices, types, max_slices)