from construct import *
from load import *
import login ; import logout ; import exit ; import logout
import summonjin

if __name__ == "__main__":
    user, password, role, nama, deskripsi, jumlah, id, pembuat, pasir, batu, air = Main()
    if user != None and password != None and role != None and nama != None and deskripsi != None and jumlah != None and id != None and pembuat != None and pasir != None and batu != None and air != None:
        username = "pass"
        role = "none"
        status = True

        while status == True:
            #load()
            opsi = input(">>> \n")
            if opsi == "help":
                help(role)

            elif opsi == "login":
                if username != "pass":
                    print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali')
                else:
                    (username, role) = login.login(user, password,role)
                
            elif opsi == "logout":
                if username == "pass":
                    print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
                else:
                    (username, role) = logout.logout()

            elif opsi == "summonjin":
                if username == "Bondowoso":
                    summonjin.summonJin()

            elif opsi == "exit":
                status = exit.exit() #True -> jalan, False -> keluar
    
