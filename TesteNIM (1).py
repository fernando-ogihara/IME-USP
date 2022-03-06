def pc_escolhe():
    n = int(input('Digite o numero n: '))
    m = int(input('Digite o numero m: '))
    pc_remove = 1
    while pc_remove != 0:
        if (n-pc_remove)%(m+1) == 0:
            return pc_remove
        else:
            pc_remove += 1
            return pc_remove

pc_escolhe()