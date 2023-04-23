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
    