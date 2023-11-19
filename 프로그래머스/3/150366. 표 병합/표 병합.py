# +5
def add(d, a, b):
    s = d.setdefault(a, set())
    s.add(b)

def remove(d, a, b):
    d.get(a, set()).discard(b)

def solution(commands):
    answer = []
    
    sheet = [['EMPTY'] * 51 for _ in range(51)]
    m = dict()

    def update(pos,value, visited):
        x = pos[0]
        y = pos[1]
        sheet[x][y] = value
        visited.add((x,y))

        for i in m.get((x,y),set()):
            if i not in visited:
                update(i, value, visited)

    def unmerge(pos, visited):
        x = pos[0]
        y = pos[1]
        visited.add(pos)
        sheet[x][y] = 'EMPTY'

        for shell in m.get((x,y),set()):
            if shell not in visited:
                unmerge(shell,visited)
        m.get(pos,set()).clear()

    for cmd in commands:
        c = cmd.split()
        query = c[0]

        if query == 'UPDATE':
            if len(c) == 4:
                x = int(c[1])
                y = int(c[2])
                update((x,y),c[3],set())
            else: # 찾아 바꾸기
                for i in range(1,51):
                    for j in range(1,51):
                        if sheet[i][j] == c[1]:
                            sheet[i][j] = c[2]

        elif query == 'MERGE':
            x1 = int(c[1])
            y1 = int(c[2])
            x2 = int(c[3])
            y2 = int(c[4])

            if x1 == x2 and y1 == y2:
                continue

            add(m,(x1,y1),(x2,y2))
            add(m,(x2,y2),(x1,y1))

            if sheet[x1][y1] != 'EMPTY' and sheet[x2][y2] != 'EMPTY':
                update((x2, y2), sheet[x1][y1], set())
            elif sheet[x1][y1] == 'EMPTY':
                update((x1, y1), sheet[x2][y2], set())
            elif sheet[x2][y2] == 'EMPTY':
                update((x2, y2), sheet[x1][y1], set())
        elif query == 'UNMERGE':
            x = int(c[1])
            y = int(c[2])
            for shell in m.get((x,y),set()):
                unmerge(shell,{(x,y)})
            m.get((x,y),set()).clear()
        elif query == 'PRINT':
            x = int(c[1])
            y = int(c[2])
            answer.append(sheet[x][y])

    return answer