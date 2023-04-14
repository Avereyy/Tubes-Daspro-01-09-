def length(lst): #len final 
    elmt = xappend(lst, "&")
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count


def dumstring(list): #mengubah list[i] menjadi str
    if length(list) == 0:
        return ""
    dumstr = str(list[0])
    index = 1
    while index < length(list):
        dumstr += "" + str(list[index])
        index += 1

    return dumstr


def xappend(lst1,lst2): #append 2 list menjadi list baru, != append
    lst = [*lst1,*lst2]
    return lst

def xlen(elmt): #fungsi untuk length
    count = 0
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&":
            count += 1

    return count

def newlist(lst): #untuk menghasilkan list tanpa & 
    elmt = xappend(lst, "&")
    final = []
    for i in range(100):
        if elmt[i] == "&":
            break
        elif elmt[i] != "&" and (i != 0):
            final = xappend(final, [elmt[i]])

    return final 

def newint(lst): #ubah list of str menjadi list of int
        i = 0
        while i < length(lst):
            lst[i] = int(lst[i])
            i += 1
        return lst

def newlist_int(lst): #newlist + newint
    xlist = newlist(lst)
    finals = newint(xlist)
    return finals

def cekstr(dumstring): #cek jika str ada \n
    newstr = ["&" for i in range(length(dumstring))]
    for i in range(length(dumstring)):
        for j in range(length(dumstring[i])):
            if dumstring[i][j] == "\n":
                break
            else:
                if newstr[i] == "&":
                    newstr[i] = str(dumstring[i][j])
                else:
                    newstr[i] += str(dumstring[i][j])
    return newstr

def write(xcsv, data): #menerima input berupa list
    with open(xcsv, 'a') as csv:
        csv_line = ';'.join(str(i) for i in data) + '\n'
        csv.write(csv_line)


def edit(xcsv, string, line): #menerima input list
    with open(xcsv) as csv: 
        data=csv.readlines()
    if line < length(data):
        data[line]= f"{string[0]};{string[1]};{string[2]} \n"
        with open(xcsv, 'w') as csv:
            csv.writelines(data)

def delete(xcsv, line):
    with open(xcsv, 'r') as csv:
        data = csv.readlines()
    if line < length(data):
        del data[line]
        with open(xcsv, 'w') as csv:
            csv.writelines(data)

#untuk user csv
with open("user.csv") as file:
    rows = file.readlines()
user = ["&" for i in range(100)]
password = ["&" for i in range(100)]
role = ["&" for i in range(100)]

char = ""
k = 0
parameter = 0

for i in range(length(rows)): 
    dumarray = rows[i]
    dumstr = dumstring(dumarray)
    for j in range(length(dumstr)): #fungsi split
        if dumstr[j] == ";":
            parameter += 1
            if parameter == 1:
                user[k] = char
                char = ""
            elif parameter == 2:
                password[k] = char
                char = ""

        elif j == (length(dumstr)-1):
                role[k] = char + dumstr[length(dumstr)-1]
                char = ""

        elif dumstr[j] != ";":
            char += dumstr[j]

    char =""
    k += 1
    parameter = 0


#untuk bahan bangunan
with open("bahan_bangunan.csv") as file_2:
    bahan = file_2.readlines()
nama = ["&" for i in range(100)]
deskripsi = ["&" for i in range(100)]
jumlah = ["&" for i in range(100)] #int

char = ""
k = 0
parameter = 0

for i in range(length(bahan)): 
    dumarray = bahan[i]
    dumstr = dumstring(dumarray)
    for j in range(length(dumstr)): #fungsi split
        if dumstr[j] == ";":
            parameter += 1
            if parameter == 1:
                nama[k] = char
                char = ""
            elif parameter == 2:
                deskripsi[k] = char
                char = ""
        elif j == (length(dumstr)-1):
                jumlah[k] = char + dumstr[length(dumstr)-1]
                char = ""

        elif dumstr[j] != ";":
            char += dumstr[j]

    char =""
    k += 1
    parameter = 0


#untuk candi
with open("candi.csv") as file_3:
    candi = file_3.readlines()
id = ["&" for i in range(100)] #int
pembuat = ["&" for i in range(100)]
pasir = ["&" for i in range(100)] #int
batu = ["&" for i in range(100)] #int
air = ["&" for i in range(100)] #int

char = ""
k = 0
parameter = 0

for i in range(length(candi)): 
    dumarray = candi[i]
    dumstr = dumstring(dumarray)
    for j in range(length(dumstr)): #fungsi split
        if dumstr[j] == ";":
            parameter += 1
            if parameter == 1:
                id[k] = char 
                char = ""
            elif parameter == 2:
                pembuat[k] = char
                char = ""
            elif parameter == 3:
                pasir[k] = char 
                char = ""
            elif parameter == 4:
                batu[k] = char 
                char = ""

        elif j == (length(dumstr)-1):
                air[k] = char + dumstr[length(dumstr)-1]
                char = ""

        elif dumstr[j] != ";":
            char += dumstr[j]

    char =""
    k += 1
    parameter = 0

