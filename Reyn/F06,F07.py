from construct import *
import random

nama = newlist(nama)
deskripsi = newlist(deskripsi)
jumlah = newlist_int(jumlah)
sisa_candi = 100

#Fungsi F07: mengumpulkan bahan
def kumpul():
    pasir = random.randint(0, 5)
    batu = random.randint(0, 5)
    air = random.randint(0, 5)
    add_pasir = jumlah[0] + pasir
    add_batu = jumlah[1] + batu
    add_air = jumlah[2] + air

    edit("bahan_bangunan.csv", ["Pasir","dari pantai",str(add_pasir)],1)
    edit("bahan_bangunan.csv", ["Batu","dari gunung",str(add_batu)],2)
    edit("bahan_bangunan.csv", ["air","dari laut",str(add_air)],3)

    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    
#Fungsi F06: membangun candi
def bahancukup(needed_pasir,needed_batu,needed_air):
    if (jumlah[0] >= needed_pasir) and (jumlah[1] >= needed_batu) and (jumlah[2] >= needed_air):
        return True
    else:
        return False

jin = "setan"
idjin = 0
def bangun():
    needed_pasir = random.randint(0, 5)
    needed_batu = random.randint(0, 5)
    needed_air = random.randint(0, 5)
    print(f"pasir: {needed_pasir} batu: {needed_batu} air: {needed_air}")
    if bahancukup(needed_pasir,needed_batu,needed_air):
        pakai_pasir = jumlah[0] - needed_pasir
        pakai_batu = jumlah[1] - needed_batu
        pakai_air = jumlah[2] - needed_air

        edit("bahan_bangunan.csv", ["Pasir","dari pantai",str(pakai_pasir)],1)
        edit("bahan_bangunan.csv", ["Batu","dari gunung",str(pakai_batu)],2)
        edit("bahan_bangunan.csv", ["air","dari laut",str(pakai_air)],3)

        global sisa_candi 
        sisa_candi = sisa_candi - 1

        print("Candi berhasil dibangun." + f"\nSisa candi yang perlu dibangun: {sisa_candi}.")
        
        global idjin
        idjin += 1

        write("candi.csv", [f"{idjin},{jin},{needed_pasir},{needed_batu},{needed_air}"])
    else:
        print("Bahan bangunan tidak mencukupi.")
