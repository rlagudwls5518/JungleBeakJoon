import sys
N, M = map(int,sys.stdin.readline().split())
tree_length=list(map(int, sys.stdin.readline().split()))

def is_possible(cut_len):
    return sum(length - cut_len for length in tree_length if length > cut_len) >= M

def bin_search(a): 
    pl = 0
    pr = max(a)
    result=0     
    while pl<=pr:
        middle=(pl+pr)//2
        if is_possible(middle):
            result = middle
            pl=middle+1
            
        else:
            pr=middle-1
    return result

print(bin_search(tree_length))