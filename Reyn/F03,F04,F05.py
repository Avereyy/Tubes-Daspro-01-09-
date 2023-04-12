#Kamus
def length(lst): #len final 
    elmt = xappend(lst, "&")
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
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


def xappend(lst1,lst2): #append 2 list menjadi list baru, != append
    lst = [*lst1,*lst2]
    return lst

def xlen(elmt): #fungsi untuk length
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count

def newlist(lst): #untuk menghasilkan list tanpa & 
    elmt = xappend(lst, "&")
    final = []
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&" and (i != 0):
            final = xappend(final, [elmt[i]])

    return final 

def newint(lst): #ubah list of str menjadi list of int
        i = 0
        while i < length(lst):
            lst[i] = int(lst[i])
            i += 1
        return lst

def newlist_int(lst): #newlist + newint
    xlist = newlist(lst)
    finals = newint(xlist)
    return finals

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

#Fungsi F03 Summonjin
#Input prosedur merupakan array_of_jin sebanyak 100
#yang terdiri dari 3 input yaitu:
array_of_jin = [[" " for j in range(0,3)] for i in range(0,100)]
#array 0 = nama, array 1 = jenis password, array 2 = jenis jin
#Sampel user
array_of_jin[99][0] = "Genie"
array_of_jin[1][0] = "GigaChad"
array_of_jin[0][0] = "MakanBang"
array_of_jin[69][0] = "420Blazeit"

array_of_jin[99][2] = str(1)
array_of_jin[1][2] = str(1)
array_of_jin[0][2] = str(2)
array_of_jin[69][2] = str(2)

def Summonjin(array_of_jin):
    #Cek jika jin array_of_jin_belum_penuh
    terisi = 0
    for i in range(0,100):
        if(array_of_jin[i][0] != " "):
            terisi = terisi + 1
    if(terisi == 100):
        print("Sudah 100 jin di-summon")
        return print("Bandung tidak dapat men-summon jin baru!") #Jika sudah penuh keluar

    #Memilih tipe jin
    print("Jenis jin yang dapat dipanggil: ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    print()
    jenis_jin = str(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    while(jenis_jin != str(1) and jenis_jin != str(2) ):
        print()
        print("Tidak ada jenis jin bernomor "+str(jenis_jin)+"!")
        print()
        jenis_jin = str(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    if(jenis_jin == str(1)):
        print("Memilih jin pengumpul")
    else: #(jenis_jin == 2):
        print("Memilih jin Pembangun")
    print()

    #Memasukan username Jin
    username_jin = input("Masukkan username jin: ")
    i = 0
    while(i < 100): #Cek jika username belum diambil
        if(array_of_jin[i][0] == str(username_jin)):
            print()
            print("Username "+str(username_jin)+" sudah diambil!")
            print()
            username_jin = input("Masukkan username jin: ")
            i = 0
        else:
            i = i + 1
    
    #Username sudah valid
    i = 0
    while(array_of_jin[i][0] != " " and i < 100): #Dimasukkan di yang kosong
        i = i + 1
    
    password_jin = input("Masukkan password jin: ")
    isPassValid = False
    while(isPassValid == False):
        if(length(password_jin) > 25 or length(password_jin) < 5):
            print()
            print("Password panjangnya harus 5-25 karakter!")
            print()
            password_jin = input("Masukkan password jin: ")
            print()
        else: #Password sudah valid
            isPassValid = True
    array_of_jin[i][0] = username_jin
    array_of_jin[i][1] = password_jin
    array_of_jin[i][2] = jenis_jin
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")
    print()
    print("Jin "+str(username_jin)+" berhasil dipanggil!")
    return

#Fungsi F04
def Hapusjin(array_of_jin):
    username_jin = str(input("Masukkan username jin : "))
    
    for i in range(0,100):#Cek unsername ada atau tidak
        if(array_of_jin[i][0] == str(username_jin)):
            confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(username_jin)+" (Y/N)?"))
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(username_jin)+" (Y/N)?"))
                print()
            if(confirm == "Y"):
                array_of_jin[i][0] = " "
                array_of_jin[i][1] = " "
                array_of_jin[i][2] = " "
                return print("Jin telah berhasil dihapus dari alam gaib.")
            else:#confirm == "N":
                return print("Jin gagal dihapus dari alam gaib.")
            
    print()
    return print("Tidak ada jin dengan username tersebut.") #Jika tidak ada

#Fungsi F05
def Ubahjin(array_of_jin):
    username_jin = str(input("Masukkan username jin : "))
    
    for i in range(0,100): #Cek unsername ada atau tidak
        if(array_of_jin[i][0] == str(username_jin)):
            if(array_of_jin[i][2] == str(1)):
                initial = "Pengumpul"
                final = "Pembangun"
                new_tipe = 2
            else: # tipe awal = pembangun
                initial = "Pembangun"
                final = "Pengumpul"
                new_tipe = 1
            
            confirm = str(input("Jin ini bertipe "+str(initial)+". Yakin ingin mengubah ke tipe "+str(final)+" (Y/N)?"))
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Jin ini bertipe Pengumpul. Yakin ingin mengubah ke tipe Pembangun (Y/N)?"))
                print()
            if(confirm == "Y"):
                array_of_jin[i][2] = str(new_tipe)
                return print("Jin telah berhasil diubah.")
            else: #Confirm == "N":
                return print("Tipe jin tidak jadi diubah.")
            
            
    print()
    return print("Tidak ada jin dengan username tersebut.") #Jika tidak ada
