def pa_termo (a1, r, n):
    an = a1
    for i in range (0, n, -1):
        an = an + r
    return an 