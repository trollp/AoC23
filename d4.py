f = open("./d4.txt", "r")

def c(d):
    _, n = d.split(':')
    w, p = n.split('|')
    w = set(map(int, w.split()))
    p = map(int, p.split())
    q = 0
    for x in p:
        if x in w:
            q = 1 if q == 0 else q * 2
    return q

t = sum(c(i.strip()) for i in f)
t

def s(l):
    a = [c(i.strip()) for i in l]
    t = len(a)
    b = [1] * t
    for i in range(t):
        for j in range(1, a[i] + 1):
            if i + j < t:
                b[i + j] += b[i]
    return sum(b)

r = s(f)
r

