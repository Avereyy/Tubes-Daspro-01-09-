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
