from construct import *
import random

nama = newlist(nama)
deskripsi = newlist(deskripsi)
jumlah = newlist_int(jumlah)

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
