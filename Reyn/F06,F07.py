from construct import *
import random

nama = newlist(nama)
deskripsi = newlist(deskripsi)
jumlah = newlist_int(jumlah)

#Fungsi F07: mengumpulkan bahan
def kumpul():
    
    with open("bahan_bangunan.csv", 'r') as csv_file:
        data = csv_file.readlines()

    pasir = random.randint(0, 5)
    batu = random.randint(0, 5)
    air = random.randint(0, 5)
    add_pasir = int(data[1].split(";")[2].strip()) + pasir
    add_batu = int(data[2].split(";")[2].strip()) + batu
    add_air = int(data[3].split(";")[2].strip()) + air

    edit("bahan_bangunan.csv", ["Pasir","dari pantai",str(add_pasir)],1)
    edit("bahan_bangunan.csv", ["Batu","dari gunung",str(add_batu)],2)
    edit("bahan_bangunan.csv", ["air","dari laut",str(add_air)],3)
    
    print(f"kumpul: Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")

    return pasir, batu, air

def kumpulprint():
    kumpul()
    print()

#Fungsi F06: membangun candi
def bahancukup(needed_pasir,needed_batu,needed_air):
    with open("bahan_bangunan.csv", 'r') as csv_file:
        data = csv_file.readlines()
    if int(data[1].split(";")[2].strip()) >= needed_pasir:
        if int(data[2].split(";")[2].strip()) >= needed_batu:
            if int(data[3].split(";")[2].strip()) >= needed_air:
                return True
                #if (jumlah[0] >= needed_pasir) and (jumlah[1] >= needed_batu) and (jumlah[2] >= needed_air):
    else:
        return False
jin = "setan"
idjin = 0
def bangun():
    needed_pasir = random.randint(0, 5)
    needed_batu = random.randint(0, 5)
    needed_air = random.randint(0, 5)
    sisa_candi = 0
    with open("candi.csv", 'r') as file_candi:
        num_rows_candi = 1
        for line in file_candi:
            num_rows_candi += 1

    if bahancukup(needed_pasir,needed_batu,needed_air):
        if num_rows_candi <= 101:
            with open("bahan_bangunan.csv", 'r') as csv_file:
                data = csv_file.readlines()

            pakai_pasir = int(data[1].split(";")[2].strip()) - needed_pasir
            pakai_batu = int(data[2].split(";")[2].strip()) - needed_batu
            pakai_air = int(data[3].split(";")[2].strip()) - needed_air

            edit("bahan_bangunan.csv", ["Pasir","dari pantai",str(pakai_pasir)],1)
            edit("bahan_bangunan.csv", ["Batu","dari gunung",str(pakai_batu)],2)
            edit("bahan_bangunan.csv", ["air","dari laut",str(pakai_air)],3)

            sisa_candi = 101 - num_rows_candi

            global idjin
            idjin += 1

            write("candi.csv", [f"{idjin};{jin};{needed_pasir};{needed_batu};{needed_air}"])
        print("Candi berhasil dibangun." + f"\nSisa candi yang perlu dibangun: {sisa_candi}.")
    else:
        print("Bahan bangunan tidak mencukupi.")

array_of_jin_pengumpul = []


def batchkumpul():
    jml_jin_pengumpul = length(array_of_jin_pengumpul)
    sum_pasir = 0
    sum_batu = 0
    sum_air = 0
    if jml_jin_pengumpul > 0:
        print(f"Mengerahkan {jml_jin_pengumpul} jin untuk mengumpulkan bahan.")
        for i in range(jml_jin_pengumpul):
            pasir, batu, air = kumpul()
            sum_pasir += pasir
            sum_batu += batu
            sum_air += air
        print(f"Jin menemukan {sum_pasir} pasir, {sum_batu} batu, dan {sum_air} air.")

    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        
array_of_jin_pembangun = ["Cacodemon", "Revenant", "Mancubus"]
