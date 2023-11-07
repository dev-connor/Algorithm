if __name__ == '__main__':
    n, m = map(int, input().split())
    arrays = []
    for _ in range(m):
        arrays.append(list(map(int, input().split())))

    baskets = [i for i in range(1,n+1)]

    for arr in arrays:
        temp = baskets[arr[0]-1]
        baskets[arr[0]-1] = baskets[arr[1]-1] 
        baskets[arr[1]-1] = temp
    
    print(' '.join(map(str, baskets)))
        

'''
5 4
1 2
3 4
1 4
2 2
'''