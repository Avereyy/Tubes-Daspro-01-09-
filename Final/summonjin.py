from construct import *
def summonjin(user, password, role):
    if length(user) >= 102:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return user, password, role
    else:
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
       
        print()
        if(jenis_jin == '1'):
            role = xappend(role, ['jin_pengumpul'])
            print('Memilih jin "Pengumpul".')
        elif(jenis_jin == '2'):
            role = xappend(role, ['jin_pembangun'])
            print('Memilih jin "Pembangun".')
        print()
        username_jin = input("Masukkan username jin: ")
        i = 0
        while(i < length(user)): #Cek jika username belum diambil
            if(username_jin == user[i]):
                print()
                print(f'Username "{str(username_jin)}" sudah diambil!')
                print()
                username_jin = input("Masukkan username jin: ")
                i = 0
            else:
                i = i + 1
    
        #Username sudah valid
        i = 0
        user = xappend(user, [str(username_jin)])
    
        password_jin = input("Masukkan password jin: ")
        isPassValid = False
        while(isPassValid == False):
            if(len(password_jin) > 25 or len(password_jin) < 5):
                print()
                print("Password panjangnya harus 5-25 karakter!")
                print()
                password_jin = input("Masukkan password jin: ")
                print()
            else: #Password sudah valid
                isPassValid = True
        password = xappend(password, [str(password_jin)])
        print()
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print()
        print("Jin "+str(username_jin)+" berhasil dipanggil!")
        return user, password, role