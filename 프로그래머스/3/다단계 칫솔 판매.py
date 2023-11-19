def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0]*n
    members = dict()

    def dfs(seller_v, amount_v):
        idx, r = members.get(seller_v)

        ten_percent = amount_v // 10
        if ten_percent != 0: # 분배할 양이 없다면
            if r != '-':
                answer[idx] += amount_v - ten_percent
                dfs(r,ten_percent) # 추천인에게 10% 분배
            else:
                answer[idx] += amount_v - ten_percent
        else: # 자신에게만 더함
            answer[idx] += amount_v

    for i,e in enumerate(enroll):
        members.setdefault(e,(i,referral[i]))

    for i,s in enumerate(seller):
        a = amount[i]*100
        dfs(s,a)

    return answer

array = []
p1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
p2 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
p3 = ["young", "john", "tod", "emily", "mary"]
p4 = [12, 4, 2, 5, 10]
result = solution(p1,p2,p3,p4)
print(result)
