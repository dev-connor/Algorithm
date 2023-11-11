# 실버5
if __name__ == '__main__':
    str = input()
    cnt = 0
    croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    i = 0

    while i < len(str):
        if i+1 < len(str) and str[i]+str[i+1] in croa:
            cnt += 1
            i += 2
        elif i+2 < len(str) and str[i]+str[i+1]+str[i+2] == 'dz=':
            cnt += 1
            i += 3
        else:
            cnt += 1
            i += 1

    print(cnt)

'''
ljes=njak
'''