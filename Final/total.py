from construct import *
def ayamberkokok(pembuat):
    candi = 0
    for i in range(length(pembuat)):
        if pembuat[i] != 'none':
            candi += 1
    
    if candi < 100:
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        print(f"Jumlah Candi: {candi}")
        print()
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print()
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        return False
    elif candi == 100:
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        print(f"Jumlah Candi: {candi}")
        print()
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        return False
    
from construct import *
import rng
def bangun(id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air ,username):

    max = 100
    if length(id) < 100:
        if pembuat[0] == 'none':
            id[0] = 0
            pembuat[0] = username
            temp = rng.RNGnoZERO(3)
            new_pasir = temp[0]
            new_batu = temp[1]
            new_air = temp[2]

            if new_pasir <= total_pasir and new_batu < total_batu and new_air < total_air:
                total_pasir -= new_pasir
                total_batu -= new_batu
                total_air -= new_air
                new_pasir = [new_pasir] ; new_batu = [new_batu] ; new_air = [new_air]
                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: {max - length(id)}.")
                return id, pembuat, new_pasir, new_batu, new_air,total_pasir, total_batu, total_air
            
            else:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun!")
                return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                
            

        elif pembuat[0] != 'none': #ubah
                for i in range(1, length(id)):
                    if (pembuat[i] == 'none'):
                        newest_id = [" "] ; new_pembuat = [" "] ; new_pasir_2 = [" "] ; new_batu_2 = [" "] ; new_air_2 = [" "]
                        max = 99

                        temp = rng.RNGnoZERO(3)
                        temp_pasir = temp[0]
                        temp_batu = temp[1]
                        temp_air = temp[2]

                        if temp_pasir <= total_pasir and temp_batu < total_batu and temp_air < total_air:
                            total_pasir -= temp_pasir
                            total_batu -= temp_batu
                            total_air -= temp_air

                            for j in range(0,i):
                                newest_id = xappend(newest_id, [id[j]])
                                new_pembuat = xappend(new_pembuat, [pembuat[j]])
                                new_pasir_2 = xappend(new_pasir_2, [pasir[j]])
                                new_batu_2 = xappend(new_batu_2, [batu[j]])
                                new_air_2 = xappend(new_air_2, [air[j]])

                            newest_id = xappend(newest_id, [newest_id[j]+1])
                            new_pembuat = xappend(new_pembuat, [username])
                            new_pasir_2 = xappend(new_pasir_2, [temp_pasir])
                            new_batu_2 = xappend(new_batu_2, [temp_batu])
                            new_air_2 = xappend(new_air_2, [temp_air])

                            for k in range(i+1, length(pembuat)):
                                newest_id = xappend(newest_id, [id[k]])
                                new_pembuat = xappend(new_pembuat, [pembuat[k]])
                                new_pasir_2 = xappend(new_pasir_2, [pasir[k]])
                                new_batu_2 = xappend(new_batu_2, [batu[k]])
                                new_air_2 = xappend(new_air_2, [air[k]])
                            print()
                            print("Candi berhasil dibangun.")
                            count = 0
                            for l in range(1,length(id)):
                                if id[l] != 0:
                                    count += 1
                            count += 1
                            print(f"Sisa candi yang perlu dibangun: {max - count}.")
                            return newest_id, new_pembuat, new_pasir_2, new_batu_2, new_air_2, total_pasir, total_batu, total_air
                            
                        else:
                            print()
                            print("Bahan bangunan tidak mencukupi.")
                            print("Candi tidak bisa dibangun!")
                            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                
                max = 99
                temp = rng.RNGnoZERO(3)
                temp_pasir = temp[0]
                temp_batu = temp[1]
                temp_air = temp[2]

                if temp_pasir <= total_pasir and temp_batu < total_batu and temp_air < total_air:
                    total_pasir -= temp_pasir
                    total_batu -= temp_batu
                    total_air -= temp_air

                    for i in range(length(id)):
                        newest_id = xappend(id, [id[i] + 1])
                    for i in range(length(id)):
                        new_pembuat = xappend(pembuat, [username])
                        new_pasir_2 = xappend(pasir, [temp_pasir])
                        new_batu_2 = xappend(batu, [temp_batu])
                        new_air_2 = xappend(air, [temp_air])
                        print()
                        print("Candi berhasil dibangun.")
                        print(f"Sisa candi yang perlu dibangun: {max - length(id)}.")
                        return newest_id, new_pembuat, new_pasir_2, new_batu_2, new_air_2,total_pasir, total_batu, total_air
                else:
                    print()
                    print("Bahan bangunan tidak mencukupi.")
                    print("Candi tidak bisa dibangun!")
                    return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

    elif length(id) >= 100:
        temp = rng.RNGnoZERO(3)
        temp_pasir = temp[0]
        temp_batu = temp[1]
        temp_air = temp[2]

        if temp_pasir <= total_pasir and temp_batu < total_batu and temp_air < total_air:
            total_pasir -= temp_pasir
            total_batu -= temp_batu
            total_air -= temp_air
            print()
            print("Candi berhasil dibangun.")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

        else:
            print()
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

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

def length(item):
    if type(item) == str:
        return len(item)
    else:
        var = str(item) ; count = 0
        for i in range(len(var)):
            if var[i] == ',':
                count += 1
    count += 1
    return count

def dumstring(list): #mengubah list[i] menjadi str
    if length(list) == 0:
        return ""
    dumstr = str(list[0])
    index = 1
    while index < length(list):
        dumstr += "" + str(list[index])
        index += 1

    return dumstr

def last(list):
    for i in range(length(list)):
        last = i
    return last

def xappend(list,var): 
    k = length(var) 
    n = length(list)
    if list == [" "]:
        n = 0
    temp = ["&" for i in range(n+k)] 
    for i in range(length(temp)-k):
        temp[i] = list[i]
    l = 0
    for j in range(length(temp)-k,length(temp),1):
        temp[j] = var[l]
        l += 1
    return temp

def newlist(lst): #untuk menghasilkan list tanpa & 
    elmt = xappend(lst, "&")
    final = [" "]
    for i in range(length(elmt)):
        if elmt[i] == "&":
            break
        elif elmt[i] != " " and (i != 0):
            final = xappend(final, [elmt[i]])

    return final 

def STRtoINT(list):
    for i in range(length(list)):
        list[i] = int(list[i])
    return list

def cekstr(dumstring): #cek jika str ada \n
    newstr = ["&" for i in range(length(dumstring))]
    for i in range(length(dumstring)):
        for j in range(length(dumstring[i])):
            if dumstring[i][j] == "\n":
                break
            else:
                if newstr[i] == "&":
                    newstr[i] = str(dumstring[i][j])
                else:
                    newstr[i] += str(dumstring[i][j])
    return newstr

def listtoone(user,password,role):  
     temp = '' 
     for i in range(length(user)):
        temp += user[i] + ';' + password[i]  + ';' + role[i] + '\n'
     return temp

def write_user(path, user, password, role):
    var = ""
    for i in range(length(user)):
        if i < length(user):
            var += user[i] + ";" + password[i] + ";" + role[i] + '\n'
        else:
            var += user[i] + ";" + password[i] + ";" + role[i]
    arr_user = "username;password;role" + '\n' + var
    with open(path, 'w') as f:
        f.write(arr_user)
    
def checkKosong(id, pembuat, pasir, batu, air):
    new_id = [" "] ;  new_pembuat = [" "] ; new_pasir = [" "] ; new_batu = [" "] ; new_air = [" "]
    initial = 0 #genti num
    for i in range(length(id)):
        while initial < id[i]:
            new_id = xappend(new_id, [0])
            new_pembuat = xappend(new_pembuat, ['none'])
            new_pasir =  xappend(new_pasir, [0])
            new_batu = xappend(new_batu, [0])
            new_air = xappend(new_air, [0])
            initial += 1
        new_id = xappend(new_id, [id[i]])
        new_pembuat = xappend(new_pembuat, [pembuat[i]])
        new_pasir =  xappend(new_pasir, [pasir[i]])
        new_batu = xappend(new_batu, [batu[i]])
        new_air = xappend(new_air, [air[i]])
        initial += 1
    return new_id, new_pembuat, new_pasir, new_batu, new_air

def write_bahan(path, pasir, batu, air):
    temp = "nama;deskripsi;jumlah" + '\n'
    var = ''
    arr_bahan = temp
    if pasir != 0 and batu != 0 and air != 0:
        pasir = "pasir;dari pantai;" + str(pasir) + '\n'
        batu = "batu;dari gunung;" + str(batu) + '\n' 
        air =  "air;dari sungai;" + str(air)
        str_bahan = pasir + batu + air
        arr_bahan += str_bahan
    else:
        arr_bahan += var

    with open(path, 'w') as f:
        f.write(arr_bahan)

def write_candi(path,id,pembuat,pasir,batu,air):
    temp = "id;pembuat;pasir;batu;air"
    var = ''
    for i in range(length(id)):
        if pembuat[i] != 'none':
            if i < length(id):
                var += str(id[i]) + ';' + pembuat[i] + ";"+ str(pasir[i]) + ";" + str(batu[i]) + ";" + str(air[i]) + '\n' 
            else:
                var += str(id[i]) + ';' + pembuat[i] + ";"+ str(pasir[i]) + ";" + str(batu[i]) + ";" + str(air[i])
    arr_candi = temp + '\n' + var
    with open(path, "w") as f:
        f.write(arr_candi)

def rupiah(angka):
    angka = str(angka)
    dum = ""; dum2 = ""
    for i in range(length(angka)):
        if i < length(angka)-3:
            dum += angka[i]
        elif i >= length(angka)-3:
            dum2 += angka[i]
    final = dum + "." + dum2
    return final

def arraysave(listuser):
    temp = ''
    for i in range(length(listuser)):
        for j in range(1):
            if i != (length(listuser)-1):
                temp += listuser[i][0] + '\n'
            else:
                temp += listuser[i][0]
    return temp

def namesort(lst):
    n = length(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


#untuk user csv
def users(csv_1):
    with open(csv_1) as file:
        rows = file.readlines()
    user = ["&" for i in range(105)]
    password = ["&" for i in range(105)]
    role = ["&" for i in range(105)]
    char = ""
    k = 0
    parameter = 0

    for i in range(length(rows)): 
        dumarray = rows[i]
        dumstr = dumstring(dumarray)
        for j in range(length(dumstr)): #fungsi split
            if dumstr[j] == ";":
                parameter += 1
                if parameter == 1:
                    user[k] = char
                    char = ""
                elif parameter == 2:
                    password[k] = char
                    char = ""
            elif j == (length(dumstr)-1):
                    role[k] = char + dumstr[length(dumstr)-1]
                    char = ""

            elif dumstr[j] != ";":
                char += dumstr[j]
        char =""
        k += 1
        parameter = 0
    return newlist(user), newlist(password), cekstr(newlist(role))

#untuk bahan bangunan
def bahan(csv_2):
    with open(csv_2) as file:
        bahan = file.readlines()
    nama = ["&" for i in range(105)]
    deskripsi = ["&" for i in range(105)]
    jumlah = ["&" for i in range(105)] #int

    char = ""
    k = 0
    parameter = 0

    for i in range(length(bahan)): 
        dumarray = bahan[i]
        dumstr = dumstring(dumarray)
        for j in range(length(dumstr)): #fungsi split
            if dumstr[j] == ";":
                parameter += 1
                if parameter == 1:
                    nama[k] = char
                    char = ""
                elif parameter == 2:
                    deskripsi[k] = char
                    char = ""
            elif j == (length(dumstr)-1):
                    jumlah[k] = char + dumstr[length(dumstr)-1]
                    char = ""

            elif dumstr[j] != ";":
                char += dumstr[j]

        char =""
        k += 1
        parameter = 0
    return newlist(nama),newlist(deskripsi), STRtoINT(cekstr(newlist(jumlah)))

#untuk candi
def candi(csv_3):

    with open(csv_3) as file:
        candi = file.readlines()
    id = ["&" for i in range(105)] #int
    pembuat = ["&" for i in range(105)]
    pasir = ["&" for i in range(105)] #int
    batu = ["&" for i in range(105)] #int
    air = ["&" for i in range(105)] #int

    char = ""
    k = 0
    parameter = 0

    for i in range(length(candi)): 
        dumarray = candi[i]
        dumstr = dumstring(dumarray)
        for j in range(length(dumstr)): #fungsi split
            if dumstr[j] == ";":
                parameter += 1
                if parameter == 1:
                    id[k] = char 
                    char = ""
                elif parameter == 2:
                    pembuat[k] = char
                    char = ""
                elif parameter == 3:
                    pasir[k] = char 
                    char = ""
                elif parameter == 4:
                    batu[k] = char 
                    char = ""

            elif j == (length(dumstr)-1):
                    air[k] = char + dumstr[length(dumstr)-1]
                    char = ""

            elif dumstr[j] != ";":
                char += dumstr[j]

        char =""
        k += 1
        parameter = 0
    return (STRtoINT(newlist(id))), (newlist(pembuat)), STRtoINT(newlist(pasir)), STRtoINT(newlist(batu)), STRtoINT(cekstr(newlist(air)))

import save
def exit(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air):
    cek = True
    while cek == True:
        ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if (ans == "y") or (ans == "Y"):
            cek = False
            save.save(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air)
            return False #True akan membuat main() terus jalan

        elif (ans == "n") or (ans == "N"):
            cek = False
            return False #False akan mengasikan nilai status di main, langsung keluar program

from construct import *

def hancur(list_id, list_pembuat, list_pasir, list_batu, list_air):
    while list_pembuat[0] != 'none':
        id = [" "] ; pembuat = [" "] ; pasir = [" "] ; batu = [" "] ; air = [" "]

        id_candi = int(input("Masukkan ID candi: "))
        for i in range(length(list_id)):
            if id_candi == list_id[i]:
                ans = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
                if ans == "Y":
                    for i in range(length(list_id)):
                        if id_candi == i:
                            id = xappend(id, [0])
                            pembuat = xappend(pembuat, ['none'])
                            pasir = xappend(pasir,[0])
                            batu = xappend(batu, [0])
                            air = xappend(air, [0])
                        elif id_candi != i:
                            id = xappend(id, [list_id[i]])
                            pembuat = xappend(pembuat, [str(list_pembuat[i])])
                            pasir = xappend(pasir, [list_pasir[i]])
                            batu = xappend(batu, [list_batu[i]])
                            air = xappend(air, [list_air[i]])
                    print()
                    print("Candi telah berhasil dihancurkan.")
                    return id, pembuat,pasir,batu,air
                else:
                    print()
                    print("Candi telah gagal dihancurkan.")
                    return list_id, list_pembuat, list_pasir, list_batu, list_air
            
            else:
                print()
                print("Tidak ada candi dengan ID tersebut.")
                return list_id, list_pembuat, list_pasir, list_batu, list_air
            
   
    print()
    print("Tidak ada candi yang telah dibuat.")
    return list_id, list_pembuat, list_pasir, list_batu, list_air

from construct import *
def hapusjin(list_user, list_pass, list_role,id,pembuat,pasir,batu,air):
    uname = input("Masukkan username jin: ") #ifrit, lala, zaki
    user = [" "] ; password = [" "] ; role = [" "]
    for i in range(length(list_user)):
        if uname == list_user[i] and (list_role[i] == "jin_pengumpul" or list_role[i] == 'jin_pembangun'):
            confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(uname)+" (Y/N)?"))
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(uname)+" (Y/N)?"))
                print()

            if confirm == "Y":
                for i in range(length(list_user)):
                    if uname != list_user[i]:
                        user = xappend(user, [str(list_user[i])])
                        password = xappend(password, [str(list_pass[i])])
                        role = xappend(role, [str(list_role[i])])
                for i in range(length(id)):
                    if uname == pembuat[i]:
                        id[i] = 0
                        pembuat[i] = 'none'
                        pasir[i] = 0
                        batu[i] = 0
                        air[i] = 0

                    
                print("Jin telah berhasil dihapus dari alam gaib.")
                return user, password, role, id, pembuat, pasir, batu, air
            else: #confirm == "N"

                print("Jin gagal dihapus dari alam gaib.")
                return list_user, list_pass, list_role, id, pembuat, pasir, batu, air

    print()
    print("Tidak ada jin dengan username tersebut.") #Jika tidak ada
    return list_user, list_pass, list_role, id, pembuat, pasir, batu, air

def help(role):
    if role == "bandung_bondowoso":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengumpulkan jin bangun")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja jin")
        print("8. laporancandi")
        print("   Untuk mengetahui proses pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data")

    elif role== "roro_jonggrang":
        print("===================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan.")
        print("4. save")
        print("   Untuk menyimpan data")
    
    elif role== "jin_pengumpul":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")

    elif role== "jin_pembangun":
        print("====================== HELP ======================")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    elif role == "none":
        print("====================== HELP ======================")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari permainan")

    else:
        return None
import rng
def kumpul(pasir, batu, air):
    temp = rng.RNGs(3)
    pasir += temp[0]
    batu += temp[1]
    air += temp[2]
    print(f"Jin mengumpulkan {temp[0]} pasir, {temp[1]} batu, dan {temp[2]} air")
    return pasir, batu, air

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

import argparse 
import os
from construct import *

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("load", help="Masukan nama folder yang ingin di load!",nargs='?')
    args = parser.parse_args()
    if args.load is None:
        print("Tidak ada nama folder yang diberikan!")
        return None,None,None,None,None,None,None,None,None,None,None,None,None
    elif os.path.isdir(args.load) == True: #cek directory ada / tidak
        print('Selamat datang di program “Manajerial Candi”')


        csv1 = args.load + '/user.csv'
        users(csv1)

        csv2 = args.load + '/bahan_bangunan.csv'
        with open(csv2) as file:
            csv_bahan  = file.readlines()
        if length(csv_bahan) == 1:
            initial = "nama;deskripsi;jumlah\n" + "pasir;dari pantai;0\n" + "batu;dari gunung;0 \n" + "air;dari sungai;0"
            with open(csv2, 'w') as f:
                f.write(initial)
        bahan(csv2)

        csv3 = args.load + '/candi.csv'
        with open(csv3) as file:
            csv_candi = file.readlines()
        if length(csv_candi) == 1:
            initial = "id;pembuat;pasir;batu;air\n" + "0;none;0;0;0"
            with open(csv3, 'w') as f:
                f.write(initial)
        candi(csv3)

        #user
        user = (users(csv1)[0])
        password = (users(csv1)[1])
        role = (users(csv1)[2])

        #Bahan_Bangunan.csv
        nama = (bahan(csv2)[0])
        deskripsi = (bahan(csv2)[1])
        total_pasir = (bahan(csv2)[2][0])
        total_batu = (bahan(csv2)[2][1])
        total_air = (bahan(csv2)[2][2])

        #candi.csv
        id = (candi(csv3)[0])
        pembuat = (candi(csv3)[1])
        pasir = (candi(csv3)[2])
        batu = (candi(csv3)[3])
        air = (candi(csv3)[4])
        return user, password, role, nama, deskripsi, id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air
    else:
        print(f"Folder “{args.load}” tidak ditemukan.")
        return None,None,None,None,None,None,None,None,None,None,None,None,None

from construct import *

def login(user, password,role):
    num  = length(user)
    username = input("Username: ")
    passw = input("Password: ")
    count = 0
    for i in range(num):
        if username != user[i]:
            count += 1
            if count == length(user):
                print("Username tidak terdaftar!")
                return("pass", "none")
        elif (username == user[i]) and (passw == password[i]):
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return(username, role[i]) 
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")
            return("pass", "none")
        
def logout():
     username = "pass"
     role = "none"
     return(username, role)

from construct import *
from load import *
import login ; import logout ; import exit ; import logout ; import help
import summonjin ; import kumpul ; import hapusjin ; import save ; import ubahjin ; import bangun ; import hancur
import batchkumpul ; import batchbangun ; import laporanjin ; import laporancandi ; import ayamberkokok

if __name__ == "__main__":
    user, password, role, nama, deskripsi, id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air = Main() #variabel total berupa int
    id, pembuat, pasir, batu, air = checkKosong(id, pembuat, pasir, batu, air)
    
    if user != None and password != None and role != None and nama != None and deskripsi != None and id != None and pembuat != None and total_pasir != None and total_batu != None and total_air != None:
        
        username = "pass"
        cekrole = "none"
        status = True
        while status == True:


            opsi = input(">>> ")
            if opsi == "help":
                help.help(cekrole)

            elif opsi == "login":
                if username != "pass":
                    print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali')
                else:
                    (username, cekrole) = login.login(user, password,role)
                
            elif opsi == "logout":
                if username == "pass":
                    print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
                else:
                    (username, cekrole) = logout.logout()

            elif opsi == "summonjin":
                if cekrole == "bandung_bondowoso":
                    user, password, role = summonjin.summonjin(user, password, role)

            elif opsi == "hapusjin":
                if cekrole == "bandung_bondowoso":
                    user,password,role,id,pembuat,pasir,batu,air = hapusjin.hapusjin(user,password,role,id,pembuat,pasir,batu,air)

            elif opsi == "ubahjin":
                if cekrole == "bandung_bondowoso":
                    user, password, role == ubahjin.ubahjin(user, password, role)

            elif opsi == "kumpul":
                if cekrole == "jin_pengumpul":
                    total_pasir, total_batu, total_air = kumpul.kumpul(total_pasir, total_batu, total_air)

            elif opsi == "batchkumpul":
                if cekrole == "bandung_bondowoso":
                    total_pasir, total_batu, total_air = batchkumpul.batchkumpul(role, total_pasir, total_batu, total_air)


            elif opsi == "hancurkancandi":
                if username == "Roro":
                    id, pembuat, pasir, batu, air = hancur.hancur(id, pembuat, pasir, batu, air)


            elif opsi == "bangun":
                if cekrole == "jin_pembangun":
                    id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air = bangun.bangun(id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air,username)

            elif opsi == "batchbangun":
                if cekrole == "bandung_bondowoso":
                    id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air = batchbangun.batchbangun(user, role, id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air)
            
            elif opsi == "laporanjin":
                if cekrole == "bandung_bondowoso":
                    laporanjin.laporan(user, role, pembuat, total_pasir, total_batu, total_air)
                elif cekrole != "bandung_bondowoso":
                    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
            
            elif opsi == "laporancandi":
                if cekrole == "bandung_bondowoso":
                    laporancandi.laporancandi(id, pembuat, pasir, batu, air)
                elif cekrole != "bandung_bondowoso":
                    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")

            elif opsi == "ayamberkokok":
                if cekrole == "roro_jonggrang":
                    status = ayamberkokok.ayamberkokok(pembuat)
            elif opsi == "save":
                save.save(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air)

            elif opsi == "exit":
                status = exit.exit(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air) #True -> jalan, False -> keluar

import time

def RNG():
    current_time = int(round(time.time() * 1000))
    return ((current_time * 1103515245 + 12345) % 2**31) / (2**31 - 1)

def RNGs(n):
    random_integers = [0] * n
    for i in range(n):
        time.sleep(0.01)
        random_integers[i] = int(RNG() * 6)
    return random_integers

def RNGnoZERO(n):
    random_integers = []
    for i in range(n):
        time.sleep(0.00001)
        random_integers.append(int(RNG() * 5) + 1)
    return random_integers

from construct import *
import os
#write, arraytostring

def save(user,password, role, total_pasir, total_batu, total_air,id,pembuat,pasir,batu,air): #file content dari array
    folderName = input("Masukkan nama folder: ")
    folder = './save/' + folderName
    if not os.path.exists('save'):
        os.mkdir('save')

    path_1 = os.path.join(folder, "user.csv")
    path_2 = os.path.join(folder, "candi.csv")
    path_3 = os.path.join(folder, "bahan_bangunan.csv")

    if not os.path.exists(folder):
        os.mkdir(folder)

    write_user(path_1, user,password,role)
    write_candi(path_2,id,pembuat,pasir,batu,air)
    write_bahan(path_3, total_pasir, total_batu, total_air)
    
from construct import *
def ubahjin(user, password, role):
    username_jin = str(input("Masukkan username jin : "))
    
    for i in range(length(user)): #Cek unsername ada atau tidak
        if(username_jin == user[i]):
            if(role[i] == "jin_pengumpul"):
                initial = "Pengumpul"
                final = "Pembangun"
                new_tipe = "jin_pembangun"
            if(role[i] == "jin_pembangun"):
                initial = "Pembangun"
                final = "Pengumpul"
                new_tipe = "jin_pengumpul"
            
            confirm = str(input("Jin ini bertipe "+str(initial)+". Yakin ingin mengubah ke tipe "+str(final)+" (Y/N)?"))
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Jin ini bertipe Pengumpul. Yakin ingin mengubah ke tipe Pembangun (Y/N)?"))
                print()
            if(confirm == "Y"):
                role[i] = str(new_tipe)
                print("Jin telah berhasil diubah.")
                return user, role, password
            else: #Confirm == "N"
                print("Tipe jin tidak jadi diubah.")
                return user, role, password
            
    print()
    print("Tidak ada jin dengan username tersebut.") #Jika tidak ada
    return user, role, password
