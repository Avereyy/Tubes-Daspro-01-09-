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

array_of_jin_pengumpul = ["Cacodemon", "Revenant", "Mancubus"]


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


def randomize():
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    c = random.randint(0, 5)
    return a,b,c 

def batchbangun():
    jml_jin_pembangun = length(array_of_jin_pembangun)
    sum_needed_pasir = 0
    sum_needed_batu = 0
    sum_needed_air = 0
    cukup = False
    if jml_jin_pembangun > 0:
        for i in range(jml_jin_pembangun):
            pasir, batu, air = randomize()
            sum_needed_pasir += pasir
            sum_needed_batu += batu
            sum_needed_air += air
            print(pasir,batu,air)
            print(sum_needed_pasir,sum_needed_batu,sum_needed_air)
            if bahancukup(sum_needed_pasir, sum_needed_batu, sum_needed_air):
                write("candi.csv", [f"{idjin};{jin};{pasir};{batu};{air}"])

        if bahancukup(sum_needed_pasir, sum_needed_batu, sum_needed_air):
            with open("bahan_bangunan.csv", 'r') as csv_file:
                data = csv_file.readlines()

            pakai_pasir = int(data[1].split(";")[2].strip()) - sum_needed_pasir
            pakai_batu = int(data[2].split(";")[2].strip()) - sum_needed_batu
            pakai_air = int(data[3].split(";")[2].strip()) - sum_needed_air

            edit("bahan_bangunan.csv", ["Pasir","dari pantai",str(pakai_pasir)],1)
            edit("bahan_bangunan.csv", ["Batu","dari gunung",str(pakai_batu)],2)
            edit("bahan_bangunan.csv", ["air","dari laut",str(pakai_air)],3)

            cukup = True

        print(f"Mengerahkan {jml_jin_pembangun} jin untuk membangun candi dengan total bahan {sum_needed_pasir} pasir, {sum_needed_batu} batu, dan {sum_needed_air} air.")
        
        if cukup == True:
            print(f"Jin berhasil membangun total {jml_jin_pembangun} candi.")
        else:
            print("Bangun gagal.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
