from construct import *

def laporancandi(id, pembuat, pasir, batu, air):
    jumlah_candi = 0 ; jumlah_pasir = 0 ; jumlah_batu = 0 ; jumlah_air = 0
    for i in range(length(id)):
        if pembuat[i] != 'none':
            jumlah_candi += 1

    if jumlah_candi > 0:
        for i in range(length(pasir)):
            jumlah_pasir += pasir[i]

        for i in range(length(batu)):
            jumlah_batu += batu[i]

        for i in range(length(air)):
            jumlah_air += air[i]

        list_harga = [" "]
        for i in range(length(id)):
            if pembuat[i] != 'none':
                harga = pasir[i] * 10000 + batu[i] * 15000 + air[i] * 7500
                list_harga = xappend(list_harga, [harga])

        matriks_harga = [[" " for i in range(2)] for i in range(length(id))]
        for i in range(length(id)):
            matriks_harga[i][0] = id[i]
            matriks_harga[i][1] = list_harga[i]

        for i in range(length(id)-1):
            for j in range(length(id)-1):
                if matriks_harga[j][1] < matriks_harga[j+1][1]:
                    matriks_harga[j], matriks_harga[j+1] = matriks_harga[j+1], matriks_harga[j]

        id_termahal = matriks_harga[0][0]
        harga_termahal = matriks_harga[0][1]

        for j in range(length(id)):
            id_termurah = matriks_harga[j][0]
            harga_termurah = matriks_harga[j][1]

        harga_termahal = rupiah(harga_termahal)
        harga_termurah = rupiah(harga_termurah)
        print()
        print(f"> Total Candi: {jumlah_candi}")
        print(f"> Total Pasir yang digunakan: {jumlah_pasir}")
        print(f"> Total Batu yang digunakan: {jumlah_batu}")
        print(f"> Total Air yang digunakan: {jumlah_air}")
        print(f"ID Candi Termahal: {id_termahal} (Rp {harga_termahal})")
        print(f"ID Candi Termurah: {id_termurah} (Rp {harga_termurah})")

    elif jumlah_candi == 0:
        print()
        print(f"> Total Candi: {jumlah_candi}")
        print(f"> Total Pasir yang digunakan: 0 ")
        print(f"> Total Batu yang digunakan: 0")
        print(f"> Total Air yang digunakan: 0")
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")
