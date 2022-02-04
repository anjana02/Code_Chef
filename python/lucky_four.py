# look for occurrences of four anywhere. 
# has a list of T integers, for each of them
# calculate the number of occurrences of the digit 4 in the decimal representation
# input : The first line of input consists of a single integer T, denoting the number of integers in list.Then, there are T lines, each of them contain a single integer from the list.
# output : Print the number of occurrences of the digit 4 in the decimal representation of each integer in the list.


def lucky_four(lst):
    count = 0
    for i in lst:
        if str(i).count('4') > 0:
            count += 1
    return count

