import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
no_duplicate = sorted(list(set(num_list)))

zip_dic = {no_duplicate[i]: i for i in range(len(no_duplicate))}

for num in num_list:
    print(zip_dic[num], end=" ")
