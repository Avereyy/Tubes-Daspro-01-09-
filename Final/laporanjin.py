from construct import *

def laporan(user, role, pembuat, total_pasir, total_batu, total_air):
    jumlah_pengumpul = 0
    jumlah_pembangun = 0
    total = 0 ; total_candi = 0
    for i in range(length(role)):
        if role[i] == "jin_pengumpul":
            jumlah_pengumpul += 1
            total += 1
        elif role[i] == 'jin_pembangun':
            jumlah_pembangun += 1
            total += 1
    for i in range(length(pembuat)):
        if pembuat[i] != 'none':
            total_candi += 1

    list_pengumpul = [" "] 
    for i in range(length(user)):
        if role[i] == "jin_pembangun":
            list_pengumpul = xappend(list_pengumpul, [user[i]])

    urutan = [0 for i in range(length(list_pengumpul))]
    for i in range(length(urutan)):
        for j in range(length(pembuat)):
            if list_pengumpul[i] == pembuat[j]:
                urutan[i] += 1

    matriks_pengumpul = [[" " for i in range(2)] for i in range(length(urutan))]
    for i in range(length(urutan)):
        matriks_pengumpul[i][0] = list_pengumpul[i]
        matriks_pengumpul[i][1] = urutan[i]


    for i in range(length(urutan)-1):
        for j in range(length(urutan)-1):
            if matriks_pengumpul[j][1] < matriks_pengumpul[j+1][1]:
                matriks_pengumpul[j], matriks_pengumpul[j+1] = matriks_pengumpul[j+1], matriks_pengumpul[j]    
    
    if total_candi == 0:
        jin_terajin = "-"
        jin_termalas = "-"


    jin_terajin = matriks_pengumpul[0][0]
    for i in range(length(urutan)):
        jin_termalas = matriks_pengumpul[i][0]

    if length(urutan) > 2:
        list_rajin = [" "] ; list_malas = [" "]
        n = matriks_pengumpul[0][1]
        for i in range(length(urutan)):
            m = matriks_pengumpul[i][1]

        for i in range(length(urutan)):
            if matriks_pengumpul[i][1] == n:
                list_rajin = xappend(list_rajin, [matriks_pengumpul[i][0]])
            elif matriks_pengumpul[i][1] == m:
                list_malas = xappend(list_malas, [matriks_pengumpul[i][0]])
                
        list_rajin = namesort(list_rajin)
        jin_terajin = list_rajin[0]
        list_malas = namesort(list_malas)
        jin_termalas = list_malas[0]

    cek = urutan[0] ; count = 0
    for i in range(length(urutan)):
        if urutan[i] == cek:
            count += 1
    if count == length(urutan):
        list_pengumpul = namesort(list_pengumpul)
        jin_terajin = list_pengumpul[0]
        for i in range(length(list_pengumpul)):
            jin_termalas = list_pengumpul[i]
        

    print(urutan)
    print(matriks_pengumpul)
    print()
    print(f"> Total Jin: {total}")
    print(f"> Total Jin Pengumpul: {jumlah_pengumpul}")
    print(f"> Total Jin Pembangun: {jumlah_pembangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {total_pasir} unit")
    print(f"> Jumlah Air: {total_air} unit")
    print(f"> Jumlah Batu: {total_batu} unit")

        
