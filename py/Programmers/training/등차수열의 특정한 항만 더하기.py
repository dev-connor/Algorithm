# +1
def solution(a, d, included):
    idxs = []

    for i,b in enumerate(included):
        if b:
            idxs.append(i)
    answer = sum(idxs)*d + a*len(idxs)

    return answer

if __name__ == '__main__':
    arr = [True, False, False, True, True]
    result = solution(3,4,arr)
    print(result)