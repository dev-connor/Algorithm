while True:
    try:
        str = input()
        print(str)
    except EOFError:
        break