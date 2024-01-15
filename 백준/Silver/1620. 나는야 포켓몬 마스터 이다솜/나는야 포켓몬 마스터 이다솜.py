n,m = map(int, input().split())
pokemons = [''] * (n+1)
d = {}
for i in range(1,n+1):
    name = input()
    pokemons[i] = name
    d.setdefault(name,i)

for i in range(m):
    input_ = input()
    if input_.isalpha():
        print(d[input_])
    else:
        print(pokemons[int(input_)])
