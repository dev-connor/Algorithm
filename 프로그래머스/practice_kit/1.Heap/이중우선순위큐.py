import heapq

# +3 - 22:23
def solution(operations):
    h = []

    for o in operations:
        do, n = o.split(' ')
        n = int(n)

        if do == 'I':
            heapq.heappush(h,n)
        else:
            if len(h) == 0:
                continue

            if n == 1:
                new_h = []
                for e in h:
                    heapq.heappush(new_h,-e)
                heapq.heappop(new_h)
                h = []
                for e in new_h:
                    heapq.heappush(h,-e)
            else:
                heapq.heappop(h)

    if len(h) == 0:
        return [0,0]

    min_n = heapq.heappop(h)
    new_h = []
    for e in h:
        heapq.heappush(new_h, -e)
    max_n = -heapq.heappop(new_h)

    return [max_n,min_n]

if __name__ == '__main__':
    array = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    array2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    result = solution(array2)
    print(result)
