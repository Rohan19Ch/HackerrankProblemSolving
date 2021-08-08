def saveThePrisoner(n, m, s):
    save = (m+s-1)%n
    if save == 0:
        return n
    else:
        return save