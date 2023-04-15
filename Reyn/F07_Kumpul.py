import random
def length(lst): #len final 
    elmt = xappend(lst, "&")
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count
def my_join(strings, delimiter): #dari chatgpt
    result = ""
    for i in range(length(strings)):
        result += strings[i]
        if i != length(strings) - 1:
            result += delimiter
    return result


def xappend(lst1,lst2):
    lst = [*lst1,*lst2]
    return lst

def my_split(string, delimiter): #dari Chatgpt
    substrings = []
    current_substring = ""
    for char in string:
        if char == delimiter:
            substrings = substrings + [current_substring]
            current_substring = ""
        else:
            current_substring += char
    substrings = substrings + [current_substring]
    return substrings

def kumpul():
    
    pasir = random.randint(0, 5)
    batu = random.randint(0, 5)
    air = random.randint(0, 5)
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    
    with open("bahan_bangunan.csv", "r") as csvfile:
        tolist = csvfile.readlines()
 
    for i in range(1, 4):
        cell = my_split(tolist[i], ",")
        if cell[0] == "Pasir":
            cell[2] = str(int(cell[2]) + pasir)
        elif cell[0] == "Batu":
            cell[2] = str(int(cell[2]) + batu)
        elif cell[0] == "air":
            cell[2] = str(int(cell[2]) + air)
        tolist[i] = my_join(cell, ",") + '\n'

    with open('bahan_bangunan.csv', 'w') as out:
        out.writelines(tolist)
