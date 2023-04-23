from construct import *

def login(user, password,role):
    num  = length(user)
    username = input("Username: ")
    passw = input("Password: ")
    count = 0
    for i in range(num):
        if username != user[i]:
            count += 1
            if count == length(user):
                print("Username tidak terdaftar!")
                return("pass", "none")
        elif (username == user[i]) and (passw == password[i]):
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return(username, role[i]) 
        elif (username == user[i]) and (passw != password[i]):
            print("Password salah!")
            return("pass", "none")