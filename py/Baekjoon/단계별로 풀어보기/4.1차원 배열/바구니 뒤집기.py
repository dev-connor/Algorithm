# 브론즈2
if __name__ == '__main__':
    n,m = map(int, input().split())
    arrays = []

    for _ in range(m):
        arrays.append(list(map(int, input().split())))

    basket = [i for i in range(n + 1)]
    new_basket = []

    for arr in arrays:
        start = arr[0]
        end = arr[1]

        new_basket = basket[:start]
        b = basket[start:end + 1]
        b.reverse()
        new_basket.extend(b)
        new_basket.extend(basket[end+1:])
        basket = new_basket
        
    print(' '.join(map(str, new_basket[1:])))

'''
5 4
1 2
3 4
1 4
2 2
'''