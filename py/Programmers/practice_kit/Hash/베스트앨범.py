def add(d, a, b):
    d.setdefault(a, 0)
    d[a] += b

def append(d, a, b):
    d.setdefault(a, [])
    d[a].append(b)

# +3 - 26:02
def solution(genres, plays):
    answer = []
    g_dict = dict()
    p_dict = dict()
    g_list = []

    for i in range(len(genres)):
        add(g_dict,genres[i],plays[i])
        append(p_dict,genres[i],(plays[i],i))

    for k,v in g_dict.items():
        g_list.append((v,k))

    g_list.sort(reverse=True)

    for sum,g in g_list:
        p_dict[g].sort(key=lambda x:(-x[0],x[1]))

        for p in p_dict[g][:2]:
            play, n = p
            answer.append(n)

    return answer

if __name__ == '__main__':
    array = []
    arr1 = ["classic", "pop", "classic", "classic", "pop"]
    arr2 = [500, 600, 150, 800, 2500]
    result = solution(arr1,arr2)
    print(result)

