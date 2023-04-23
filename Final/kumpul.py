import rng
def kumpul(pasir, batu, air):
    temp = rng.RNGs(3)
    pasir += temp[0]
    batu += temp[1]
    air += temp[2]
    print(f"Jin mengumpulkan {temp[0]} pasir, {temp[1]} batu, dan {temp[2]} air")
    return pasir, batu, air
