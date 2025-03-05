import math

#mencari volume kubus
def VKubus (s):
    return s * s * s

#mencari volume balok
def Vbalok (p, l, t):
    return p * l * t

#mencari volume bola
def VBola (r):
    return 4/3 * 3.14 * r**3

#mencari volume prisma
def VPrisma (LA, t):
    return LA * t