import time

def RNG():
    current_time = int(round(time.time() * 1000))
    return ((current_time * 1103515245 + 12345) % 2**31) / (2**31 - 1)

def RNGs(n):
    random_integers = [0] * n
    for i in range(n):
        time.sleep(0.01)
        random_integers[i] = int(RNG() * 6)
    return random_integers

def RNGnoZERO(n):
    random_integers = []
    for i in range(n):
        time.sleep(0.00001)
        random_integers.append(int(RNG() * 5) + 1)
    return random_integers