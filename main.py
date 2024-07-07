n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

variance = k1 - k2

bol = k1 - m

perc = bol / variance

print(n - int(n * perc), int(n * perc))
