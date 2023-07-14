def berlekamp_massey(seq):
    L, m, b = 0, 1, [1]
    for n in range(len(seq)):
        d = seq[n] + sum([seq[n-i-1] * b[i] for i in range(L)])
        if d == 0:
            m += 1
        elif 2 * L <= n:
            b = b + [0] * (m-L-1) + [-d//m]
            L, m = n+1-L, 1
        else:
            b = b + [0] * (n-L) + [-d//m]
            m += 1
    return b

seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
coefficients = berlekamp_massey(seq)
print("The coefficients are:", coefficients)
