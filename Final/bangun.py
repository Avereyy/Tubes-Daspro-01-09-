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