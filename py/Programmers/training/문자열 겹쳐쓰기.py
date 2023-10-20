def solution(my_string, overwrite_string, s):
    prefix = my_string[:s]
    suffix = my_string[s + len(overwrite_string):]

    return prefix + overwrite_string + suffix

if __name__ == '__main__':
    str1 = "He11oWor1d"
    str2 = "lloWorl"
    result = solution(str1, str2, 2)
    print(result)

