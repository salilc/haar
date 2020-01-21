import math   

def haar_resolution(wave):
    base = 1 / 2**0.5
    n = len(wave) // 2
    a = [base*(wave[2*i] + wave[2*i+1]) for i in range(0, n)]
    d = [base*(wave[2*i] - wave[2*i+1]) for i in range(0, n)]
    return a, d
    

def haar(wave):
    n = int(math.log(len(wave), 2))
    a = wave[:2**(n)]
    decomp = []
    while True:
        a, d = haar_resolution(a)
        decomp.append(d)
        if len(a) == 1:
            decomp.append(a)
            break
    decomp.reverse()
    return decomp

def inverse_haar_resolution(a, d):
    decomp = []
    base = 1 / 2**0.5
    for i in range(0, len(a)):
        decomp.append(base*(a[i] + d[i]))
        decomp.append(base*(a[i] - d[i]))
    return decomp


def inverse_haar(h):
    res = h[0]
    for i in range(1, len(h)):
        res = inverse_haar_resolution(res, h[i])
    return res







