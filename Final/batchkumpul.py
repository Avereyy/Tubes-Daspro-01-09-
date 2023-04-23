from construct import *
import rng

def kumpul():
    temp = rng.RNGs(3)
    return temp

def batchkumpul(role, total_pasir, total_batu, total_air):
    n = 0
    pasir = 0 ; batu = 0 ; air = 0
    for i in range(length(role)):
        if role[i] == "jin_pengumpul":
            n += 1
    if n != 0:
        for i in range(n):
            pasir += (kumpul()[0])
            batu += (kumpul()[1])
            air += (kumpul()[2])
            
        total_pasir += pasir
        total_batu += batu
        total_air += air

        print(f"Mengerahkan {n} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
        return total_pasir , total_batu , total_air

    elif n == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return total_pasir ,total_batu , total_air
