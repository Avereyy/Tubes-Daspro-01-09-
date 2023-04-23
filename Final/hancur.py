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
