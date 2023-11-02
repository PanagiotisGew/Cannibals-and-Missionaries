start,end =[3,3,1],[0,0,0]

# 
def kane_kinisi(katastash,kinisi):
    if katastash[2] == 1:
        return [katastash[i] - kinisi[i] for i in range(3)]
    else:
        return [katastash[i] + kinisi[i] for i in range(3)]

def an_epitrepete(katastash):
    if 0 <= katastash[0] <= 3 and 0 <= katastash[1] <= 3:
        return True
    else:
        return False

def an_einai_asfales(bank):
    if bank[1] > bank[0] and bank[0] != 0:
        return False
    else:
        return True

def is_katastash_safe(katastash):
    other_bank = [start[i]-katastash[i] for i in range(3)]
    if an_einai_asfales(katastash) and an_einai_asfales(other_bank) :
        return True
    else:
        return False

def epomeni_dinati_kinisi(katastash):
    actions = [[1,0,1],[0,1,1],[1,1,1],[2,0,1],[0,2,1]]
    moves = []
    for i in actions:
        j = kane_kinisi(katastash,i)
        if an_epitrepete(j) and is_katastash_safe(j):
            moves.append(j)
    return moves

solutions = []
def solve(epomeni_kinisi,path):
    _path = path.copy()
    if epomeni_kinisi == end:
        _path.append(epomeni_kinisi)
        solutions.append(_path)
        return
    elif epomeni_kinisi in path:
        return
    else:
        _path.append(epomeni_kinisi)
        for i in epomeni_dinati_kinisi(epomeni_kinisi):
            solve(i,_path)

solve([3,3,1],[])
print(*solutions,sep="\n")