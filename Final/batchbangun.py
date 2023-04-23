from construct import *
import rng

def batchbangun(user, role, id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air):
    list_user = [' ']
    for j in range(length(role)):
        if role[j] == "jin_pembangun":
            list_user =  xappend(list_user, [user[j]])
    
    if list_user != [' ']: 
        jumlah_pasir = 0 ; jumlah_batu = 0 ; jumlah_air = 0
        list_pasir = [" "] ; list_batu = [" "]; list_air = [" "]
        for j in range(length(list_user)):
            temp = rng.RNGnoZERO(3)
            jumlah_pasir += temp[0]
            list_pasir = xappend(list_pasir, [temp[0]])
            jumlah_batu += temp[1]
            list_batu = xappend(list_batu, [temp[1]])
            jumlah_air += temp[2]
            list_air = xappend(list_air, [temp[2]])

        if (jumlah_pasir <= total_pasir) and (jumlah_batu <= total_batu) and (jumlah_air <= total_air):
            total_pasir -= jumlah_pasir
            total_batu -= jumlah_batu
            total_air -= jumlah_air

            count = 0 ; check = False ; checknone = False
            if pembuat[0] == 'none' and pasir[0] == 0 and batu[0] == 0 and air[0] == 0:
                id[0] = 0
                pembuat[0] = list_user[0]
                pasir[0] = list_pasir[0]
                batu[0] = list_batu[0]
                air[0] = list_air[0]
                count += 1 ; check = True

            if pembuat[0] != 'none':
                countnone = 0
                for l in range(1, length(id)):
                        if pembuat[l] == 'none':
                            countnone += 1
                        if check == False:
                            if countnone <= length(list_user):
                                if pembuat[l] == 'none' :
                                    id[l] = id[l-1] + 1
                                    pembuat[l] = list_user[count]
                                    pasir[l] = list_pasir[count]
                                    batu[l] = list_batu[count]
                                    air[l] = list_air[count]
                                    count += 1
                                    checknone = True
                        elif check == True:
                            if countnone < length(list_user):
                                if pembuat[l] == 'none' :
                                    id[l] = id[l-1] + 1
                                    pembuat[l] = list_user[count]
                                    pasir[l] = list_pasir[count]
                                    batu[l] = list_batu[count]
                                    air[l] = list_air[count]
                                    count += 1
                                    checknone = True

                if count < length(list_user):
                    if check == True: 
                        if checknone == True:
                            for i in range(length(list_user)-count):
                                id = xappend(id, [last(id) + 1])

                            for i in range(length(list_user)-count):
                                pembuat = xappend(pembuat, [list_user[count]])
                                pasir = xappend(pasir, [list_pasir[count]])
                                batu = xappend(batu, [list_batu[count]])
                                air = xappend(air, [list_air[count]])
                                count += 1
                        elif checknone == False:
                            for i in range(length(list_user)-1):
                                id = xappend(id, [last(id) + 1])

                            for i in range(length(list_user)-1):
                                pembuat = xappend(pembuat, [list_user[count]])
                                pasir = xappend(pasir, [list_pasir[count]])
                                batu = xappend(batu, [list_batu[count]])
                                air = xappend(air, [list_air[count]])
                                count += 1

                    elif check == False:
                        if checknone == True:
                            for i in range(length(list_user)-count):
                                id = xappend(id, [last(id) + 1])

                            for i in range(length(list_user)-count):
                                pembuat = xappend(pembuat, [list_user[count]])
                                pasir = xappend(pasir, [list_pasir[count]])
                                batu = xappend(batu, [list_batu[count]])
                                air = xappend(air, [list_air[count]])
                                count += 1

                        elif checknone == False:
                            for i in range(length(list_user)):
                                id = xappend(id, [last(id) + 1])

                            for i in range(length(list_user)):
                                pembuat = xappend(pembuat, [list_user[count]])
                                pasir = xappend(pasir, [list_pasir[count]])
                                batu = xappend(batu, [list_batu[count]])
                                air = xappend(air, [list_air[count]])
                                count += 1

            print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air


        else:
            print(f"Bangun gagal. Kurang {(jumlah_pasir - total_pasir)} pasir, {jumlah_batu - total_batu} batu, dan {jumlah_air - total_air} air.")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air 


    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air