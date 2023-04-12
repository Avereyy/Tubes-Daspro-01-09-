import time

def RNG(xo, a, b): #Pilih 3 parameter, lebih baik jika prima dan besar
    angka_acak = [0 for i in range(100)]
    for i in range(99):
        angka_acak[0] = xo
        m = 6
        angka_acak[i+1] = (a * angka_acak[i] +b) % m

    return(angka_acak[50])

def generate_seed():
    seed = int(round(time.time() * 1000))
    return seed


def kumpul():
    # Generate random quantities of sand, stone, and water
    
    pasir = RNG(generate_seed(), 50497,676)
    batu = RNG(generate_seed(), 40031, 107)
    air = RNG(generate_seed(), 30091, 149)


    jml_pasir = 0
    jml_batu = 0
    jml_air = 0
    # Add the generated quantities to the global material counts
    jml_pasir += pasir
    jml_batu += batu
    jml_air += air

    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return jml_air, jml_batu, jml_pasir  #sementara, nanti dimasukkan csv
