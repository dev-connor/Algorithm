# 실버5
if __name__ == '__main__':
    inputs = []
    for _ in range(20):
        inputs.append(list(input().split()))

    g = {
        'A+':	4.5,
        'A0':	4.0,
        'B+':	3.5,
        'B0':	3.0,
        'C+':	2.5,
        'C0':	2.0,
        'D+':	1.5,
        'D0':	1.0,
        'F':    0.0,
    }

    total = 0
    c_sum = 0

    for subject,credit,grade in inputs:
        if grade == 'P':
            continue

        total += g[grade]*float(credit)
        c_sum += float(credit)

    print(total/c_sum)
