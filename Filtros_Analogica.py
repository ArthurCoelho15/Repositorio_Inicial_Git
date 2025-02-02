import math

a = 1.414214
b = 1
C = 10/30000
wc = 2 * math.pi * C
dentro = (pow(a,2) + 8*b*1.5) * wc

R1 = 4*b / (a + math.sqrt(dentro) * wc * C)

R2 = b / pow(wc,2) * pow(C,2) * R1

R3 = 2.5 * R1 / 1.5

R4 = 2.5 * R1

K = 1 + R4/R3

print(round(R1, 4))
print(round(R2, 4))
print(round(R3, 4))
print(round(R4, 4))
print(C)
print(K)