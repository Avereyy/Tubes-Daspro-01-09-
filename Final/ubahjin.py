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
